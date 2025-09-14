from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel, HttpUrl, Field

class Headline(BaseModel):
    title: str
    source: str
    url: HttpUrl
    published_date: Optional[str] = Field(None, description="YYYY-MM-DD")

class SummaryItem(BaseModel):
    title: str
    source: str
    url: HttpUrl
    summary: str

class Headlines(BaseModel):
    headlines: List[Headline]

class Summaries(BaseModel):
    summaries: List[SummaryItem]

class Insights(BaseModel):
    insights: List[str]