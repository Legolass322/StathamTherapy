from fastapi import APIRouter
from .auth.all import router as auth_router
from .chat.all import router as chat_router

router = APIRouter(prefix="/api")

router.include_router(auth_router)
router.include_router(chat_router)
