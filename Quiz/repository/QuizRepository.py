from dataclasses import dataclass
import logging
from typing import Any

from sqlmodel import Session, select
from entity.QuizEntity import Quiz


@dataclass
class QuizRepository:
    database: Any

    def create_quiz(self, quiz: Quiz):
        with Session(self.database) as session:
            statement = select(Quiz).where(Quiz.id == quiz.id)
            result = session.exec(statement).first()

            if result == None:
                session.add(quiz)
                session.commit()
                session.refresh(quiz)
                return quiz

            return None

    def get_quizzes(self):
        with Session(self.database) as session:
            quizzes = session.exec(select(Quiz)).all()

            if quizzes != []:
                return quizzes

            return None

    def get_quiz(self, quiz_id: int):
        with Session(self.database) as session:

            quiz = session.get(Quiz, quiz_id)

            if not quiz:
                return None

            return quiz

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
