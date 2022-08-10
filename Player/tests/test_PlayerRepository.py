from typing import List
import pytest
from sqlmodel import Session, SQLModel, create_engine

from repository.PlayerRepository import PlayerRepository
from entity.PlayerEntity import Player

# create test engine
testEngine = create_engine("postgresql://postgres@localhost:5432/testingdb")
SQLModel.metadata.create_all(testEngine)


# create mockRepository
mockRepository = PlayerRepository(testEngine)


@pytest.fixture
def mock_player():
    '''Returns a Player instance'''
    return Player(id=1, name="Toh Wei", email="tohwei@xiang.com", points=0,
                  categories_played={
                      "Movies": 1,
                      "Kdrama": 5
                  })


@pytest.fixture
def updated_mock_player():
    '''Returns a updated Player instance'''
    return Player(id=1, name="Toh Wei updated", email="tohwei@xiang.com-updated", points=0,
                  categories_played={
                      "Movies": 1,
                      "Kdrama": 5
                  })


def test_create_player(mock_player):

    # create mock Player object
    result = mockRepository.create_player(mock_player)

    assert result == mock_player


def test_create_player_failed(mock_player):

    # create the same player which should return None
    result = mockRepository.create_player(mock_player)

    assert result is None


def test_get_players(mock_player):

    mock_player_list = [mock_player]

    result = mockRepository.get_players()

    assert result == mock_player_list


def test_get_player(mock_player):

    result = mockRepository.get_player(1)

    assert result == mock_player


def test_update_player(updated_mock_player):

    result = mockRepository.update_player(updated_mock_player)

    assert result.id == updated_mock_player.id
    assert result.name == updated_mock_player.name
    assert result.email == updated_mock_player.email
    assert result.points == updated_mock_player.points
    assert result.categories_played == updated_mock_player.categories_played


def test_delete_player(updated_mock_player):

    # delete player via id that has already been created
    result = mockRepository.delete_player(1)

    assert result == updated_mock_player


def test_delete_player_failed():

    # attempt delete player via id that does not exist
    result = mockRepository.delete_player(1)

    assert result is None


def test_get_players_failed():

    result = mockRepository.get_players()

    assert result is None


def test_get_player_failed():

    result = mockRepository.get_player(1)

    assert result is None


def test_update_player_failed(updated_mock_player):

    result = mockRepository.update_player(updated_mock_player)

    assert result is None
