from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def welcome():
    return "Hello World!"
