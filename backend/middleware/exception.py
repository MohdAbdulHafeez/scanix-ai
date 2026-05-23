from fastapi import Request
from fastapi.responses import ORJSONResponse

from core.logging import app_logger


async def global_exception(
    request: Request,
    exc: Exception,
):

    app_logger.exception(
        exc
    )

    return ORJSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": str(
                exc
            ),
        },
    )