import time

from starlette.middleware.base import BaseHTTPMiddleware


class TimingMiddleware(
    BaseHTTPMiddleware
):

    async def dispatch(
        self,
        request,
        call_next,
    ):

        started = (
            time.time()
        )

        response = await call_next(
            request
        )

        elapsed = round(
            (
                time.time()
                - started
            )
            * 1000,
            2,
        )

        response.headers[
            "X-Process-Time"
        ] = str(
            elapsed
        )

        return response