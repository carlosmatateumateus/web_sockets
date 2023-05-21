from fastapi import APIRouter, Request, WebSocket, WebSocketDisconnect
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from .manager import ws_manager

class Message(BaseModel):
    message: str

duplex_router = APIRouter()
templates = Jinja2Templates(directory='templates')

@duplex_router.get('/duplex')
def route(request: Request, response_class=HTMLResponse):
    return templates.TemplateResponse(
        'duplex.html', {'request': request}
    )

@duplex_router.post('/duplex')
async def route_b(message: Message, response_model=Message):
    ...
    # Implementação do WebSockets
    await ws_manager.broadcast(message.message)
    return {'message': 'ok'}

@duplex_router.websocket('/ws/duplex/{user}')
async def duplex_endpoint(websocket: WebSocket, user: str):
    await ws_manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await ws_manager.broadcast(data)
    except WebSocketDisconnect:
        ws_manager.disconnect(websocket)