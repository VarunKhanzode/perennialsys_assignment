from fastapi import FastAPI
from app.api.routes import router
from app.core.db import Base, engine

app = FastAPI(title="Employee Search API", version="1.0.0")

Base.metadata.create_all(bind=engine)

app.include_router(router)
