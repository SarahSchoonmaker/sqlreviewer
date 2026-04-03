from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="SQL Intelligence Platform")

app.include_router(router)