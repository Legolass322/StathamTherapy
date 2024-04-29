from fastapi import Depends

from database.models.user import User
from app.providers.user.deps import get_current_user
from .router import router

@router.get('/me', summary='Get details of currently logged in user')
async def get_me(user: User = Depends(get_current_user)):
    return user