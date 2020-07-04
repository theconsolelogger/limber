from fastapi import FastAPI
from limber.routes.api import router as api_router

app = FastAPI()

app.include_router(api_router)
