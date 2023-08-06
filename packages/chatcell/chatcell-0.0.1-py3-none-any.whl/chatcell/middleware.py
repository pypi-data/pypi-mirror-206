import json

from fastapi import HTTPException, Request
from starlette.middleware.base import BaseHTTPMiddleware

import chatcell

logger = chatcell.get_logger("app")


class LoggingMiddleware(BaseHTTPMiddleware):
    async def set_body(self, request: Request):
        receive_ = await request._receive()

        async def receive():
            return receive_

        request._receive = receive

    async def dispatch(self, request: Request, call_next):
        logger.info(f"Request: {request.method} {request.url}")
        try:
            # Per https://github.com/tiangolo/fastapi/issues/394#issuecomment-927272627
            # to avoid blocking.
            await self.set_body(request)
            body = await request.json()
            logger.debug(f"Request body: {json.dumps(body)}")
        except json.JSONDecodeError:
            logger.error("Request body: Unable to parse JSON")

        response = await call_next(request)

        logger.info(f"Response status: {response.status_code}")
        try:
            if hasattr(response, "body"):
                body = json.loads(response.body.decode())
                logger.debug(f"Response body: {json.dumps(body)}")
        except json.JSONDecodeError:
            logger.error("Response body: Unable to parse JSON")

        return response


def exception_handler(request: Request, ex: HTTPException):
    logger.error(ex)
