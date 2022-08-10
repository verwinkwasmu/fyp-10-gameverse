from dataclasses import dataclass
from entity.PlayerEntity import Player
from repository.PlayerRepository import PlayerRepository


@dataclass
class PlayerService:
    repository: PlayerRepository

    def create_player(self, player: Player):
        result = self.repository.create_player(player)

        if result != None:
            return result

        return None

    def get_players(self):
        result = self.repository.get_players()

        if result != None:
            return result

        return None

    def get_player(self, player_id: int):
        result = self.repository.get_player(player_id)

        if result != None:
            return result

        return None

    def update_player(self, player: Player):
        result = self.repository.update_player(player)

        if result != None:
            return result

        return None

    def delete_player(self, player_id: int):
        result = self.repository.delete_player(player_id)

        if result != None:
            return result

        return None
