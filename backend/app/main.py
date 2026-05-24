"""
SCANIX AI
Production FastAPI Application
"""

from contextlib import asynccontextmanager
from pathlib import Path
import time

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse
from fastapi.staticfiles import StaticFiles

from app.router import router
from core.logging import app_logger
from core.settings import settings
from middleware.request_id import RequestIDMiddleware
from middleware.timing import TimingMiddleware
from middleware.exception import global_exception


STARTED_AT = time.time()


# ==========================================================
# CREATE GENERATED FOLDER
# ==========================================================

Path(
    "generated/voice"
).mkdir(
    parents=True,
    exist_ok=True,
)


@asynccontextmanager
async def lifespan(
    app: FastAPI,
):

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
# STATIC AUDIO SERVING
# ==========================================================

app.mount(

    "/generated",

    StaticFiles(

        directory="generated"

    ),

    name="generated",

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


app.add_middleware(
    RequestIDMiddleware
)

app.add_middleware(
    TimingMiddleware
)

app.add_exception_handler(
    Exception,
    global_exception,
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

            time.time()
            -
            STARTED_AT,

            2,

        ),

    }