"""
SCANIX AI
Health & diagnostics endpoints
"""

import time

from fastapi import APIRouter

from core.settings import settings


router = APIRouter(
    prefix="/health",
    tags=["health"],
)

STARTED = time.time()


@router.get("")
async def health():

    return {
        "success": True,
        "service": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENV,
        "status": "healthy",
    }


@router.get("/ready")
async def readiness():

    return {
        "success": True,
        "ready": True,
    }


@router.get("/live")
async def liveness():

    uptime = round(
        time.time() - STARTED,
        2,
    )

    return {
        "success": True,
        "uptime_seconds": uptime,
    }