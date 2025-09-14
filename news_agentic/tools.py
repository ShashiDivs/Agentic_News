from __future__ import annotations
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, WebsiteSearchTool

def get_search_tool():
    # SerperDevTool reads SERPER_API_KEY from env
    return SerperDevTool()

def get_site_search_tool():
    return WebsiteSearchTool()

def get_scrape_tool():
    return ScrapeWebsiteTool()