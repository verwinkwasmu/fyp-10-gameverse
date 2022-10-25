from dataclasses import dataclass
import logging
from typing import Any
from unicodedata import category

from sqlmodel import Session, select
from entity.QuestionEntity import Question
from entity.QuizEntity import Quiz


@dataclass
class QuizRepository:
    database: Any

    def create_quiz(self, quiz: Quiz):
        with Session(self.database) as session:
            statement = select(Quiz).where(Quiz.id == quiz.id)
            result = session.exec(statement).first()

            if result == None:
                self.save_questions(quiz, session)
                session.add(quiz)
                session.commit()
                session.refresh(quiz)
                return quiz

            return None

    def get_quizzes(self):
        with Session(self.database) as session:
            quizzes = session.exec(select(Quiz)).all()
            print(quizzes)
            if quizzes or quizzes == []:
                return quizzes

            return None

    def get_quiz(self, quiz_id: int):
        with Session(self.database) as session:

            quiz = session.get(Quiz, quiz_id)

            if not quiz:
                return None

            return quiz

    def get_user_quizzes(self, user_id: int):
        with Session(self.database) as session:
            statement = select(Quiz).where(Quiz.user_id == user_id)
            quizzes = session.exec(statement).all()

            if quizzes or quizzes == []:
                return quizzes

            return None

    def update_quiz(self, quiz: Quiz):
        with Session(self.database) as session:
            result = session.get(Quiz, quiz.id)

            if not result:
                return None

            quiz_data = quiz.dict(exclude_unset=True)
            for key, value in quiz_data.items():
                setattr(result, key, value)

            session.add(result)
            session.commit()
            session.refresh(result)

            return result

    def delete_quiz(self, quiz_id: id):
        with Session(self.database) as session:

            quiz = session.get(Quiz, quiz_id)
            if not quiz:
                return None

            session.delete(quiz)
            session.commit()

            return quiz

    def save_questions(self, quiz: Quiz, session: Session):

        for question in quiz.questions:
            """
            Checking if question already exist in the question db
            """
            existing_question = session.exec(
                select(Question).where(Question.title == question.get("question"))
            ).first()

            if not existing_question:
                option = question.get("options")
                data = Question(
                    title=question.get("question"),
                    option_1=option.get("option_1"),
                    option_2=option.get("option_2"),
                    option_3=option.get("option_3"),
                    option_4=option.get("option_4"),
                    answer=question.get("answer"),
                    timer=question.get("timer"),
                    category=quiz.category,
                )
                session.add(data)

    def get_questions(self, category: str):
        with Session(self.database) as session:
            questions = session.exec(
                select(Question).where(Question.category == category)
            ).all()

            if questions != []:
                return questions

            return None

    def get_category(self, category: str):
        with Session(self.database) as session:
            print(category)
            if category == "":
                results = session.exec(select(Question.category).distinct()).all()
            else:
                results = [
                    session.exec(
                        select(Question.category).where(
                            Question.category == category.capitalize()
                        )
                    ).first()
                ]

            if results != []:
                return results

            return None
