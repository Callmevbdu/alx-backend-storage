#!/usr/bin/env python3
"""
Module docstring: This module provides functions to fetch and cache web
pages.
"""
import requests
import redis
from functools import wraps
r = redis.Redis()


def get_page(url: str) -> str:
    """Fetches the HTML content of a URL and caches it."""
    r.incr(f"count:{url}")
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    url = 'http://slowwly.robertomurray.co.uk'
    page_content = get_page(url)
    print(page_content)
