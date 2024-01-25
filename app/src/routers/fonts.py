from typing import List 
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session 
from ..dependencies import get_token_header, get_db 
from ..domain.user import service, schemas 



router = APIRouter(
    prefix="/fonts", 
    tags=["items"], 
    responses={404: {"description": "Not Found"}}
)

@router.get("/")
def get_fonts():
    return {"gitu": "nggakgitu"}