import os
from tobrot.sample_config import Config

class Config(Config):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
    APP_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH")
    OWNER_ID = int(os.environ.get("OWNER_ID", 12345))
    AUTH_CHANNEL = set(
        int(x) for x in os.environ.get(
            "AUTH_CHANNEL", "").split())
