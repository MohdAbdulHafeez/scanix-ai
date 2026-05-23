"""
SCANIX AI
Production FastAPI Application
"""

from contextlib import asynccontextmanager
import time

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse

from app.router import router
from core.logging import app_logger
from core.settings import settings


STARTED_AT = time.time()


@asynccontextmanager
async def lifespan(app: FastAPI):

    app_logger.info(
        f"Starting {settings.APP_NAME}"
    )

    yield

    app_logger.info(
        f"Stopping {settings.APP_NAME}"
    )


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="AI Food Intelligence Platform",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
    default_response_class=ORJSONResponse,
)


# ==========================================================
# CORS
# ==========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        settings.FRONTEND_URL,
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==========================================================
# ROUTERS
# ==========================================================

app.include_router(
    router
)


# ==========================================================
# ROOT
# ==========================================================

@app.get(
    "/",
    tags=["system"],
)
async def root():

    return {
        "success": True,
        "service": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENV,
    }


@app.get(
    "/status",
    tags=["system"],
)
async def status():

    return {
        "success": True,
        "uptime_seconds": round(
            time.time() - STARTED_AT,
            2,
        ),
    }