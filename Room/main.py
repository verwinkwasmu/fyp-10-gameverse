from dataclasses import asdict

from typing import Dict, List

from fastapi import FastAPI, WebSocket, WebSocketDisconnect

from entities import MessageResponse, User

app = FastAPI()


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
        # self.current_users: List[User] = []
        self.current_users: Dict[int, User] = {}
        self.currentCount: int = 0

    async def connect(self, websocket: WebSocket, user_id: int, user: User):
        await websocket.accept()
        self.active_connections.append(websocket)
        self.current_users[user_id] = user

    def disconnect(self, websocket: WebSocket, user_id: str):
        self.active_connections.remove(websocket)
        del self.current_users[user_id]

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, messageResponse: MessageResponse):
        for connection in self.active_connections:
            await connection.send_json(asdict(messageResponse))


# need to create multiple connectionManager based on room_id currently using this way
currentConnections = {}


@app.websocket("/ws/{room_id}/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: int, room_id: int):

    if room_id not in currentConnections:
        currentConnections[room_id] = ConnectionManager()

    manager = currentConnections.get(room_id)

    # create user entity
    user = User(name=user_id, score=0)

    await manager.connect(websocket, user_id, user)

    messageResponse = MessageResponse(
        command="Join",
        message=f"User #{user_id} has entered the game room #{room_id}!",
        current_users=manager.current_users,
    )
    await manager.broadcast(messageResponse)

    try:
        while True:
            data = await websocket.receive_json()

            # if data received is 'Done'
            if data["command"] == "Done":
                manager.currentCount += 1

                # update the scores
                manager.current_users[user_id].score += data['score']

                if manager.currentCount == len(manager.active_connections):
                    manager.currentCount = 0
                    messageResponse = MessageResponse(
                        command="Next Question",
                        message="Moving to the next question...",
                        current_users=manager.current_users,
                    )

            elif data['command'] == 'Scoreboard':
                messageResponse = MessageResponse(
                    command="",
                    message="show scoreboard",
                    current_users=manager.current_users
                )

            await manager.broadcast(messageResponse)

    except WebSocketDisconnect:
        manager.disconnect(websocket, user_id)
        messageResponse = MessageResponse(
            command="Leave",
            message=f"User #{user_id} left the game room",
            current_users=manager.current_users,
        )
        await manager.broadcast(messageResponse)

        # remove current websocket connection from Connection Channel
        if not manager.active_connections:
            del currentConnections[room_id]
