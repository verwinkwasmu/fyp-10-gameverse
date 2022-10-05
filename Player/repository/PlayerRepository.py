from dataclasses import dataclass
from typing import Any
from unicodedata import category

from sqlmodel import Session, select
from entity.PlayerEntity import QuizResult
from entity.PlayerEntity import Player


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
            player = session.get(Player, quizResults.id)

            if not player:
                return None

            player.total_points += quizResults.score

            categories_played = player.categories_played

            ## try the hero.dict(exclude_unset=True)
            player_data = player.dict()
            for key, value in player_data.items():
                print(key)
            if quizResults.category not in player.categories_played:
                categories_played[quizResults.category] = {
                    "count": 1,
                    "points": quizResults.score,
                }
                # setattr(
                #     player,
                #     "categories_played",
                #     categories_played,
                # )
                player.categories_played = categories_played
            else:
                categories_played[quizResults.category]["count"] += 1
                categories_played[quizResults.category]["points"] += quizResults.score
                setattr(player, "categories_played", categories_played)

            print(player)
            session.add(player)
            session.commit()
            session.refresh(player)
            print("updated hero:", player)
            return player
