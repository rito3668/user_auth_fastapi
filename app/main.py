from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from sqlmodel import SQLModel
import logging
import time 
from app.db import models
from app.db.database import engine
from app.routers import users
from app.routers import auth
app = FastAPI()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
@app.exception_handler(Exception)
async def global_exception_handler(request:Request,exc:Exception):
    return JSONResponse(
        status_code=500,
        content={"detail":"Internal Server error. Please try again later!"}
    )

@app.middleware("http")
async def log_requests(request,call_next):
    start_time = time.time()
    logger.info(f"Incoming request: {request.method} {request.url.path}")
    response = await call_next(request)
    process_time = round((time.time()-start_time)*1000,2)
    logger.info(
        f"Completed {request.method} {request.url.path} "
        f"in {process_time}ms with status {response.status_code}"
    )
    return response

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

app.include_router(users.router,prefix="/users",tags=["Users"])
app.include_router(auth.router,prefix="/auth",tags=["Auth"])
@app.get("/")
def root():
    return {
        "message":" Database is ready!"
    }
