class ConnectionManager:
    def __init__(self):
        self.connections = []

    async def connect(self, websocket):
        await websocket.accept()
        self.connections.append(websocket)

    async def broadcast(self, message):
        for con in self.connections:
            await con.send_text(message)

    def disconnect(self, websocket):
        self.connections.remove(websocket)


ws_manager = ConnectionManager()