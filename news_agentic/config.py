from __future__ import annotations
import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv(override=True)

@dataclass(frozen=True)
class Settings:
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    serper_api_key: str = os.getenv("SERPER_API_KEY", "")
    default_topic: str = os.getenv("NEWS_TOPIC", "Technology policy")
    max_articles: int = int(os.getenv("MAX_ARTICLES", "8"))
    recency_days: int = int(os.getenv("RECENCY_DAYS", "14"))

settings = Settings()