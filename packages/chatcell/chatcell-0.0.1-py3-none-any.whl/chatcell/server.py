from typing import Any, Dict

from fastapi import Depends, FastAPI, HTTPException, Request, Response
from fastapi.exceptions import RequestValidationError
from fastapi.responses import HTMLResponse
from sse_starlette.sse import EventSourceResponse

from chatcell.base import ChatcellHandler
from chatcell.middleware import LoggingMiddleware, exception_handler
from chatcell.types import (QueryRequest, ReportErrorRequest,
                            ReportFeedbackRequest, SettingsRequest)


def get_bot(handler: ChatcellHandler) -> None:
    """
    Run a Chatcell bot server using FastAPI.

    :param handler: The bot handler, should inheriate from class `ChatcellHandler`.
    :param api_key: The Chatcell API key to use. If not provided, it will try to read
    the CHATCELL_API_KEY environment. If that is not set, the server will not require
    authentication.

    """
    app = FastAPI()
    app.add_exception_handler(RequestValidationError, exception_handler)

    @app.get("/")
    async def index() -> Response:
        return HTMLResponse(
            "<html><body><h1>FastAPI Chatcell bot server</h1><p>Congratulations! Your server"
            " is running. Soon you can connect it on pickpickrole.ai."
        )

    @app.post("/")
    async def chatcell_post(request: Dict[str, Any]) -> Response:
        if request["type"] == "query":
            return EventSourceResponse(
                handler.handle_query(QueryRequest.parse_obj(request))
            )
        elif request["type"] == "settings":
            return await handler.handle_settings(SettingsRequest.parse_obj(request))
        elif request["type"] == "report_feedback":
            return await handler.handle_report_feedback(
                ReportFeedbackRequest.parse_obj(request)
            )
        elif request["type"] == "report_error":
            return await handler.handle_report_error(
                ReportErrorRequest.parse_obj(request)
            )
        else:
            raise HTTPException(status_code=501, detail="Unsupported request type")

    return app


def run(handler: ChatcellHandler):
    import uvicorn

    # init app
    app = get_bot(handler)

    # init logger
    # Uncomment this line to print out request and response
    # app.add_middleware(LoggingMiddleware)

    # run app
    uvicorn.run(app, host="0.0.0.0", port=8080)
