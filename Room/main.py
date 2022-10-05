from dataclasses import asdict

from typing import Dict, List

from fastapi import FastAPI, WebSocket, WebSocketDisconnect

from entities import MessageResponse, User

app = FastAPI()


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self.current_users: Dict[int, User] = {}
        self.quiz_id: int = None

    async def connect(self, websocket: WebSocket, user_id: int, user: User):
        await websocket.accept()
        self.active_connections.append(websocket)
        self.current_users[user_id] = user

    def disconnect(self, websocket: WebSocket, user_id: str):
        self.active_connections.remove(websocket)
        del self.current_users[user_id]

    async def send_personal_message(self, message: int, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, messageResponse: MessageResponse):
        for connection in self.active_connections:
            await connection.send_json(asdict(messageResponse))


# need to create multiple connectionManager based on room_id currently using this way
currentConnections = {}


@app.websocket("/ws/{room_id}/{user_id}/{quiz_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: int, room_id: int, quiz_id):

    if room_id not in currentConnections:
        currentConnections[room_id] = ConnectionManager()

    manager = currentConnections.get(room_id)

    # create user entity
    user = User(name=user_id, score=0)

    await manager.connect(websocket, user_id, user)

    if quiz_id != "undefined":
        manager.quiz_id = quiz_id
    else:
        await manager.send_personal_message(manager.quiz_id, websocket)

    messageResponse = MessageResponse(
        command="Join",
        current_users=manager.current_users,
    )
    await manager.broadcast(messageResponse)

    try:
        while True:
            data = await websocket.receive_json()

            match data["command"]:
                case "Done":
                    manager.current_users[user_id].score += data["score"]

                case "Next Question":
                    messageResponse = MessageResponse(
                        command="Next Question",
                        current_users=manager.current_users,
                    )
                    await manager.broadcast(messageResponse)

                case "Scoreboard":
                    messageResponse = MessageResponse(
                        command="Show Scoreboard",
                        current_users=manager.current_users,
                    )
                    await manager.broadcast(messageResponse)

                case "Start":
                    messageResponse = MessageResponse(
                        command="Start Game",
                        current_users=manager.current_users,
                    )
                    await manager.broadcast(messageResponse)

                case "To Podium":
                    messageResponse = MessageResponse(
                        command="To Podium",
                        current_users=manager.current_users,
                    )
                    await manager.broadcast(messageResponse)

    except WebSocketDisconnect:
        manager.disconnect(websocket, user_id)
        messageResponse = MessageResponse(
            command="Leave",
            current_users=manager.current_users,
        )
        await manager.broadcast(messageResponse)

        # remove current websocket connection from Connection Channel
        if not manager.active_connections:
            del currentConnections[room_id]
