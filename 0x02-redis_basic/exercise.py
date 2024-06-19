#!/usr/bin/env python3
"""
This module provides a Cache class for storing and retrieving data from a Redis
server.
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    The Cache class encapsulates methods for storing and retrieving data using
    Redis.
    """


    def __init__(self):
        """
        Initialize the Cache instance with a Redis client connection and flush
        the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()


    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis using a random key and return the key.
        """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key
