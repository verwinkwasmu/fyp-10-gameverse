from typing import List
import pytest
from sqlmodel import Session, SQLModel, create_engine

from repository.QuizRepository import QuizRepository
from entity.QuizEntity import Quiz

# create test engine
testEngine = create_engine("postgresql://postgres@localhost:5432/testingdb")
SQLModel.metadata.create_all(testEngine)


# create mockQuizRepository
mockQuizRepository = QuizRepository(testEngine)


@pytest.fixture
def mock_quiz():
    '''Returns a Quiz instance'''
    return Quiz(id=1, title="Test-Title", category="Test-Category",
                questions={"test-question": "test-option"})


@pytest.fixture
def updated_mock_quiz():
    '''Returns a updated Quiz instance'''
    return Quiz(id=1, title="Updated-Title", category="Updated-Category",
                questions={"updated-question": "updated-option"})


def test_create_quiz(mock_quiz):

    # create mock Quiz object
    result = mockQuizRepository.create_quiz(mock_quiz)

    assert result == mock_quiz


def test_create_quiz_failed(mock_quiz):

    # create the same quiz which should return None
    result = mockQuizRepository.create_quiz(mock_quiz)

    assert result is None


def test_get_quizzes(mock_quiz):

    mock_quiz_list = [mock_quiz]

    result = mockQuizRepository.get_quizzes()

    assert result == mock_quiz_list


def test_get_quiz(mock_quiz):

    result = mockQuizRepository.get_quiz(1)

    assert result == mock_quiz


def test_update_quiz(updated_mock_quiz):

    result = mockQuizRepository.update_quiz(updated_mock_quiz)

    assert result.id == updated_mock_quiz.id
    assert result.category == updated_mock_quiz.category
    assert result.questions == updated_mock_quiz.questions
    assert result.title == updated_mock_quiz.title


def test_delete_quiz(updated_mock_quiz):

    # delete quiz via id that has already been created
    result = mockQuizRepository.delete_quiz(1)

    assert result == updated_mock_quiz


def test_delete_quiz_failed():

    # attempt delete quiz via id that does not exist
    result = mockQuizRepository.delete_quiz(1)

    assert result is None


def test_get_quizzes_failed():

    result = mockQuizRepository.get_quizzes()

    assert result is None


def test_get_quiz_failed():

    result = mockQuizRepository.get_quiz(1)

    assert result is None


def test_update_quiz_failed(updated_mock_quiz):

    result = mockQuizRepository.update_quiz(updated_mock_quiz)

    assert result is None
