from pydantic import SecretStr
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    BOT_TOKEN: SecretStr
    MONGODB_URL: SecretStr
    MONGODB_DB: SecretStr
    OPENAI_KEY: SecretStr
    SENTRY_URL: SecretStr
    SOCKS_PROXY: SecretStr
    HTTP_PROXY: SecretStr

    GEMINI_API_KEY: SecretStr
    LOGGING_CHAT: str

    CHAT_COMPLETION_MAX_TOKENS: int
    CHAT_COMPLETION_TIMEOUT: int
    CHAT_COMPLETION_STREAM_INTERVAL: float
    DEFAULT_GPT_MODEL: str
    DEFAULT_IMG_MODEL: str

    YOOKASSA_ACCOUNT_ID: SecretStr
    YOOKASSA_SECRET_KEY: SecretStr
    DEFAULT_SUBSCRIPTION: str

    FAL_AI_API_KEY: SecretStr

SETTINGS = Settings(_env_file=".env", _env_file_encoding="utf-8")