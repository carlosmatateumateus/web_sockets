from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .static import static_router
from .dynamic import dynamic_router
from .push import push_router
from .duplex import duplex_router

app = FastAPI()

app.include_router(static_router)
app.include_router(dynamic_router)
app.include_router(push_router)
app.include_router(duplex_router)


app.mount(
    '/static',
    StaticFiles(directory='static'),
    name='static'
 )

