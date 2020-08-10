from fastapi import APIRouter, Request
from limber.app.http.controllers import welcome_controller

router = APIRouter()

@router.get('/')
def welcome(request: Request):
    return welcome_controller.get()
