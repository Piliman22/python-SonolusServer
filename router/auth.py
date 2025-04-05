from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse,Response
from datetime import datetime, timedelta
import secrets

router = APIRouter()
# めっちゃ簡単な認証だから改善あり(たぶん)
@router.post('/sonolus/authenticate')
async def authenticate():
    session = secrets.token_urlsafe(32)
    
    expiration = int((datetime.now() + timedelta(days=1)).timestamp() * 1000)
    
    return JSONResponse(
        content={
            "session": session,
            "expiration": expiration
        },
        status_code=status.HTTP_200_OK
    )