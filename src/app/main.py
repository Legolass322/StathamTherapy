from contextlib import asynccontextmanager
import time
from typing import Awaitable, Callable
from fastapi import FastAPI, Request, Response

from database import database
from .routes.api import api_router

from logger.logger import logger

from config.config import config


@asynccontextmanager
async def lifespan(_: FastAPI):
    logger.info("Lifespan start")
    database.db.init(config["database"]["host"])
    database.db.create_tables()
    yield
    logger.info("Lifespan end")


app = FastAPI(lifespan=lifespan)

@app.middleware("http")
async def request_info(request: Request, call_next: Callable[[Request], Awaitable[Response]]):
    logger.info(f"Request started: {request.method} {request.url}")
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    logger.info(f"Request finished: {request.method} {request.url} in {process_time}s")
    return response

app.include_router(api_router.router)
