from fastapi import FastAPI

from app.apis.v1.api import v1_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


app.include_router(v1_router, tags=["v1"], prefix="/api/v1")
