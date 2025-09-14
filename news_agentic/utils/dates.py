from __future__ import annotations
from datetime import datetime, timedelta

def today_str() -> str:
    return datetime.now().strftime("%Y-%m-%d")

def cutoff_days(days: int) -> str:
    return (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
