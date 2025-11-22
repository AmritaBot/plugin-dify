from nonebot import logger, require
from nonebot.plugin import PluginMetadata

require("amrita.plugins.chat")


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

logger.info("[Dify] Succeed to load plugin amrita_plugin_dify")
