from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel


class Message(BaseModel):
    message: str

dynamic_router = APIRouter()
templates = Jinja2Templates(directory='templates')

@dynamic_router.get('/dynamic')
def route(request: Request, response_class=HTMLResponse):
    return templates.TemplateResponse(
        'dynamic.html', {'request':request}
    )

@dynamic_router.get('/dynamic/data')
def route_b(request: Request, response_model=Message):
    from random import randint

    return {'message': randint(0, 100)}


@dynamic_router.get('/polling')
def route_c(request: Request, response_class=HTMLResponse):
    return templates.TemplateResponse(
        'polling.html', {'request':request}
    )