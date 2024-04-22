from fastapi import FastAPI
from .routes.api import api_router

app = FastAPI()


app.include_router(api_router.router)


@app.get("/")
async def root():
    return {"message": "Hello, World from FastAPI!"}
