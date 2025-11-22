import json
import typing

from amrita.plugins.chat.API import ToolContext, on_tools
from dify_client import AsyncClient, models
from nonebot import logger

from .config import CONFIG
from .models import RAG_TOOL_DATA


@on_tools(RAG_TOOL_DATA, strict=True, custom_run=True)
async def rag_tool(ctx: ToolContext) -> str | None:
    """
    Use Dify to search for an answer to a query.

    Success => Return the answer(json {"success": true, "answer": "Answer"})
    Failed => Return the error message(json {"success": false, "error": "Error message"})
    """
    if not CONFIG.dify_enabled:
        logger.info("[Dify] Plugin is not enabled, skipping tool...")
        return
    try:
        query: dict[str, str] = ctx.data
        event = ctx.event.get_nonebot_event()
        uid = f"amrita-u-{event.get_user_id()}"
        logger.info(f"[Dify] Searching for uid@{uid} answer to query: {query['query']}")
        client = AsyncClient(api_key=CONFIG.dify_api_key, api_base=CONFIG.dify_api_base)
        request = models.ChatRequest(
            query=query["query"], user=uid, response_mode=models.ResponseMode.BLOCKING
        )
        response = typing.cast(
            models.ChatResponse, await client.achat_messages(request)
        )
        logger.info(
            f"[Dify] Got answer: `{response.answer}` for uid@{uid} query: {query['query']}"
        )
        return json.dumps({"success": True, "answer": response.answer})
    except Exception as e:
        logger.opt(exception=e, colors=True).exception(
            "[Dify] Error occurred while searching for answer"
        )
        return json.dumps({"success": False, "error": str(e)})
