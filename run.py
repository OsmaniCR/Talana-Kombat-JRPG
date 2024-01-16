from fastapi import FastAPI
import uvicorn
from controllers.game_controller import get_fight_history
from models.game_model import GameModel

app = FastAPI(title="Talana-Kombat-JRPG API")

@app.get("/")
def say_hi():
    return {"OsmaniCR says": "Welcome to Talana-Kombat"}


@app.post("/game")
def lets_play(json_fight: GameModel):
    return get_fight_history(json_fight)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8008)
