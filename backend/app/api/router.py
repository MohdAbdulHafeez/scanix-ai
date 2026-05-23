"""
SCANIX API Router
"""

from fastapi import APIRouter

from app.api.v1.health import (
    router as health_router,
)

from app.api.v1.barcode import (
    router as barcode_router,
)

from app.api.v1.explain import (
    router as explain_router,
)


api_router = APIRouter()


api_router.include_router(
    health_router
)


api_router.include_router(
    barcode_router
)


api_router.include_router(
    explain_router
)