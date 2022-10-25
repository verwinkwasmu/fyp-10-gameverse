import logging
from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlmodel import Field, Session, SQLModel, create_engine, select
from fastapi.middleware.cors import CORSMiddleware
from entity.QuestionEntity import Question

from repository.QuizRepository import QuizRepository
from service.QuizService import QuizService
from entity.QuizEntity import Quiz

engine = create_engine(
    "postgresql://postgres:TysBv8mr0Am4FN6D7cyj@containers-us-west-60.railway.app:5748/railway"
)




def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# can only be used in fastapi routes.. so not sure if its a wise design to pass through this every layer


def get_session():
    with Session(engine) as session:
        yield session


app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# set up classes
quizRepository = QuizRepository(engine)
quizService = QuizService(quizRepository)

# set log level
logging.basicConfig(level=logging.DEBUG)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/api/quizzes/", response_model=List[Quiz])
async def get_quizzes():
    quizzes = quizService.get_quizzes()

    if quizzes is None:
        raise HTTPException(status_code=500, detail="No quizzes found")

    return quizzes


@app.get("/api/quizzes/user/{user_id}", response_model=List[Quiz])
async def get_user_quizzes(user_id: int):
    quizzes = quizService.get_user_quizzes(user_id)

    if quizzes is None:
        raise HTTPException(
            status_code=500, detail=f"No quizzes found for user with id: {user_id}"
        )

    return quizzes


@app.get("/api/quiz/{quiz_id}", response_model=Quiz)
async def get_quiz(quiz_id: int):
    quiz = quizService.get_quiz(quiz_id)

    if quiz is None:
        raise HTTPException(
            status_code=500, detail=f"quiz with id: {quiz_id} not found"
        )

    return quiz


@app.post("/api/create/", response_model=Quiz)
async def create_quiz(quiz: Quiz):
    result = quizService.create_quiz(quiz)

    if result == None:
        raise HTTPException(
            status_code=500, detail=f"Unable to create quiz for id: {quiz.id}"
        )

    return result


@app.put("/api/update/", response_model=Quiz)
async def update_quiz(quiz: Quiz):
    result = quizService.update_quiz(quiz)

    if result is None:
        raise HTTPException(
            status_code=500, detail=f"Unable to update quiz with id: {quiz.id}"
        )

    return result


@app.delete("/api/delete/{quiz_id}", response_model=Quiz)
async def delete_quiz(quiz_id: int):
    result = quizService.delete_quiz(quiz_id)

    if result is None:
        raise HTTPException(
            status_code=500, detail=f"Unable to delete quiz for id: {quiz_id}"
        )

    return result


@app.get("/api/questions/{category}", response_model=List[Question])
async def get_questions(category: str):
    result = quizService.get_questions(category)

    if result is None:
        raise HTTPException(
            status_code=500, detail=f"questions with category {category} not found"
        )

    return result


@app.get("/api/category/")
async def get_category(category: str = ""):
    results = quizService.get_category(category)

    if results is None:
        raise HTTPException(status_code=500, detail="No category found")

    return results
