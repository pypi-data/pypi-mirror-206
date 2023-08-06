import json
from typing import AsyncIterable, Dict, Optional, Union

from fastapi.responses import JSONResponse
from sse_starlette.sse import ServerSentEvent

from chatcell.types import (ContentType, QueryRequest, ReportErrorRequest,
                            ReportFeedbackRequest, SettingsRequest,
                            SettingsResponse)

from .logging import get_logger

logger = get_logger("app")


class ChatcellHandler:
    # Override these for your bot

    async def get_response(self, query: QueryRequest) -> AsyncIterable[ServerSentEvent]:
        """Override this to return a response to user queries."""
        yield self.text_event("hello")

    async def get_settings(self, setting: SettingsRequest) -> SettingsResponse:
        """Override this to return non-standard settings."""
        return SettingsResponse()

    async def on_feedback(self, feedback_request: ReportFeedbackRequest) -> None:
        """Override this to record feedback from the user."""
        logger.debug(f"Feedback from Chatcell user: {feedback_request}")

    async def on_error(self, error_request: ReportErrorRequest) -> None:
        """Override this to record errors from the Chatcell server."""
        logger.error(f"Error from Chatcell server: {error_request}")

    # Helpers for generating responses

    @staticmethod
    def text_event(text: str) -> ServerSentEvent:
        return ServerSentEvent(data=json.dumps({"text": text}), event="text")

    @staticmethod
    def replace_response_event(text: str) -> ServerSentEvent:
        return ServerSentEvent(
            data=json.dumps({"text": text}), event="replace_response"
        )

    @staticmethod
    def done_event() -> ServerSentEvent:
        return ServerSentEvent(data="{}", event="done")

    @staticmethod
    def suggested_reply_event(text: str) -> ServerSentEvent:
        return ServerSentEvent(data=json.dumps({"text": text}), event="suggested_reply")

    @staticmethod
    def meta_event(
        *,
        content_type: ContentType = "text/markdown",
        refetch_settings: bool = False,
        linkify: bool = True,
        suggested_replies: bool = True,
    ) -> ServerSentEvent:
        return ServerSentEvent(
            data=json.dumps(
                {
                    "content_type": content_type,
                    "refetch_settings": refetch_settings,
                    "linkify": linkify,
                    "suggested_replies": suggested_replies,
                }
            ),
            event="meta",
        )

    @staticmethod
    def error_event(
        text: Optional[str] = None, *, allow_retry: bool = True
    ) -> ServerSentEvent:
        data: Dict[str, Union[bool, str]] = {"allow_retry": allow_retry}
        if text is not None:
            data["text"] = text
        return ServerSentEvent(data=json.dumps(data), event="error")

    # Internal handlers

    async def handle_report_feedback(
        self, feedback_request: ReportFeedbackRequest
    ) -> JSONResponse:
        await self.on_feedback(feedback_request)
        return JSONResponse({})

    async def handle_report_error(
        self, error_request: ReportErrorRequest
    ) -> JSONResponse:
        await self.on_error(error_request)
        return JSONResponse({})

    async def handle_settings(self, settings_request: SettingsRequest) -> JSONResponse:
        settings = await self.get_settings(settings_request)
        return JSONResponse(settings.dict())

    async def handle_query(self, query: QueryRequest) -> AsyncIterable[ServerSentEvent]:
        async for event in self.get_response(query):
            yield event
        yield self.done_event()
