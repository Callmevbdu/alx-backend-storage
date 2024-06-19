#!/usr/bin/env python3
"""
This module provides a Cache class for storing and retrieving data from a
Redis server.
"""
import redis
import uuid
from typing import Union, Callable, Optional


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

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:  # noqa
        """
        Retrieve the stored data by key and convert it using the provided
        Callable.
        """
        value = self._redis.get(key)
        if fn is not None and value is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a string value by key from Redis.
        """
        return self.get(key, fn=lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer value by key from Redis.
        """
        value = self.get(key)
        return int(value) if value is not None else None
