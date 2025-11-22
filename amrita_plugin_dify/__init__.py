from nonebot import require
from nonebot.plugin import PluginMetadata

require("amrita.plugins.chat")
from amrita.plugins.chat.API import config_manager
from amrita.plugins.chat.hook_manager import register_hook


@register_hook
async def _():
    await config_manager.register_config("dify_enabled", True)


from . import search

__plugin_meta__ = PluginMetadata(
    name="DifyExtension",
    description="Dify extension for Amrita",
    usage="Read the README.md for more information.",
    type="library",
    homepage="https://github.com/AmritaBot/plugin-dify",
    supported_adapters=None,  # Support all adapters
)


__all__ = ["search"]
