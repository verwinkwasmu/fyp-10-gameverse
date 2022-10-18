from dataclasses import dataclass
from entity.QuizEntity import Quiz
from repository.QuizRepository import QuizRepository


@dataclass
class QuizService:
    repository: QuizRepository

    def create_quiz(self, quiz: Quiz):
        result = self.repository.create_quiz(quiz)

        if result != None:
            return result

        return None

    def get_quizzes(self):
        result = self.repository.get_quizzes()

        if result != None:
            return result

        return None

    def get_quiz(self, quiz_id: int):
        result = self.repository.get_quiz(quiz_id)

        if result != None:
            return result

        return None

    def update_quiz(self, quiz: Quiz):
        result = self.repository.update_quiz(quiz)

        if result != None:
            return result

        return None

    def delete_quiz(self, quiz_id: int):
        result = self.repository.delete_quiz(quiz_id)

        if result != None:
            return result

        return None

    def get_questions(self, category: str):
        result = self.repository.get_questions(category)

        if result != None:
            return result

        return None

    def get_category(self, category: str):
        result = self.repository.get_category(category)

        if result != None:
            return result

        return None
