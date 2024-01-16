from typing import Union, List
from pydantic import BaseModel

class PlayerModel(BaseModel):
    movimientos: List[str]
    golpes: List[str]

class GameModel(BaseModel):
    player1: PlayerModel
    player2: PlayerModel