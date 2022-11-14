from dataclasses import dataclass
from typing import Any
from unicodedata import category
from xxlimited import new

from sqlmodel import Session, select
from entity.PlayerEntity import QuizResult
from entity.PlayerEntity import Player

from copy import deepcopy

@dataclass
class PlayerRepository:
    database: Any

    def create_player(self, player: Player):
        with Session(self.database) as session:
            statement = select(Player).where(Player.id == player.id)
            result = session.exec(statement).first()

            if result == None:
                session.add(player)
                session.commit()
                session.refresh(player)
                return player

            return None

    def get_players(self):
        with Session(self.database) as session:
            players = session.exec(select(Player)).all()

            if players != []:
                players.sort(key=lambda x: x.total_points, reverse=True)
                return players

            return None

    def get_player(self, player_id: int):
        with Session(self.database) as session:

            player = session.get(Player, player_id)

            if not player:
                return None

            return player

    def update_player(self, player: Player):
        with Session(self.database) as session:
            result = session.get(Player, player.id)

            if not result:
                return None

            player_data = player.dict(exclude_unset=True)

            for key, value in player_data.items():
                setattr(result, key, value)

            session.add(result)
            session.commit()
            session.refresh(result)

            return result

    def delete_player(self, player_id: id):
        with Session(self.database) as session:

            player = session.get(Player, player_id)
            if not player:
                return None

            session.delete(player)
            session.commit()

            return player

    def input_quiz_results(self, quizResults: QuizResult):
        with Session(self.database) as session:
            oldPlayer = session.get(Player, quizResults.id)

            if not oldPlayer:
                return None

            # add start end times
            if oldPlayer.start_times == None:
                oldPlayer.start_times = []
            if oldPlayer.end_times == None:
                oldPlayer.end_times = []

            new_start_times = oldPlayer.start_times + [quizResults.start_time]
            end_start_times = oldPlayer.end_times + [quizResults.end_time]

            oldPlayer.start_times = new_start_times
            oldPlayer.end_times = end_start_times

            oldPlayer.total_points += quizResults.score

            player = deepcopy(oldPlayer)

            # this requires a copy to work
            new_categories_played = player.categories_played

            if quizResults.category not in new_categories_played:
                new_categories_played[quizResults.category] = {}

            if quizResults.quizTitle not in new_categories_played[quizResults.category]:
                new_categories_played[quizResults.category][quizResults.quizTitle] = {
                    "count": 1,
                    "points": quizResults.score,
                }
            else:
                new_categories_played[quizResults.category][quizResults.quizTitle][
                    "count"
                ] += 1
                new_categories_played[quizResults.category][quizResults.quizTitle][
                    "points"
                ] += quizResults.score

            setattr(oldPlayer, "categories_played", new_categories_played)
            
            session.add(oldPlayer)
            session.commit()
            session.refresh(oldPlayer)

            return oldPlayer
