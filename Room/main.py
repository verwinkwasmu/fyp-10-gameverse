from dataclasses import asdict, dataclass
from dataclasses_json import dataclass_json

from typing import List

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

app = FastAPI()

# responses
@dataclass
class User:
    name: str
    user_id: int
    score: int


@dataclass
class MessageResponse:
    command: str
    message: str
    current_users: List[User]


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self.current_users: List[User] = []
        self.currentCount: int = 0

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, messageResponse: MessageResponse):
        for connection in self.active_connections:
            await connection.send_json(asdict(messageResponse))


# need to create multiple connectionManager based on room_id currently using this way
currentConnections = {}


@app.websocket("/ws/{room_id}/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str, room_id: int):

    if room_id not in currentConnections:
        currentConnections[room_id] = ConnectionManager()

    manager = currentConnections.get(room_id)

    await manager.connect(websocket)

    manager.current_users.append(User(user_id=user_id, name="", score=0))

    messageResponse = MessageResponse(
        command="Join",
        message=f"User #{user_id} has entered the game room #{room_id}!",
        current_users=manager.current_users,
    )
    await manager.broadcast(messageResponse)

    try:
        while True:
            data = await websocket.receive_text()

            # if data received is 'Done'
            if data == "Done":
                manager.currentCount += 1

                if manager.currentCount == len(manager.active_connections):
                    manager.currentCount = 0
                    messageResponse = MessageResponse(
                        command="Next Question",
                        message="Moving to the next question...",
                        current_users=manager.current_users,
                    )
                    await manager.broadcast(messageResponse)

                # await manager.send_personal_message(f"You wrote: {data}", websocket)
                # await manager.broadcast(f"User #{user_id} says: {data}")

    except WebSocketDisconnect:
        manager.disconnect(websocket)
        messageResponse = MessageResponse(
            command="Leave",
            message=f"User #{user_id} left the game room",
            current_users=manager.current_users,
        )
        await manager.broadcast(messageResponse)
