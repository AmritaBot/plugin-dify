from nonebot import require
from nonebot.plugin import PluginMetadata

from . import search

__plugin_meta__ = PluginMetadata(
    name="DifyExtension",
    description="Dify extension for Amrita",
    usage="Read the README.md for more information.",
    type="library",
    homepage="https://github.com/AmritaBot/plugin-dify",
    supported_adapters=None,  # Support all adapters
)

require("amrita.plugins.chat")

__all__ = ["search"]
