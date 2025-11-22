from nonebot import get_plugin_config
from pydantic import BaseModel


class Config(BaseModel):
    """Dify plugin Configuration
    DIFY_API_KEY =>  Your Dify API Key
    DIFY_API_BASE => Your Dify API URL
    DIFY_ENABLED => Enable Dify Plugin
    """

    dify_api_key: str
    dify_api_base: str = "https://api.dify.ai/v1"
    dify_enabled: bool = False


CONFIG = get_plugin_config(Config)
