#!/usr/bin/env python3
"""
This module provides a Cache class for storing and retrieving data from a
Redis server.
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts how many times methods of the Cache class are called.
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator that stores the history of inputs and outputs for a particular
    function.
    """
    inputs_key = f"{method.__qualname__}:inputs"
    outputs_key = f"{method.__qualname__}:outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.rpush(inputs_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, str(result))
        return result

    return wrapper


class Cache:
    """
    The Cache class encapsulates methods for storing and retrieving data
    using Redis.
    """

    def __init__(self):
        """
        Initialize the Cache instance with a Redis client connection and flush
        the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis using a random key and return the key.
        """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str) -> Union[str, bytes]:
        """
        Retrieve the stored data by key from Redis.
        """
        value = self._redis.get(key)
        return value if value is not None else None


def replay(method: Callable):
    """
    Function that displays the history of calls of a particular function.
    """
    qualified_name = method.__qualname__
    inputs_key = f"{qualified_name}:inputs"
    outputs_key = f"{qualified_name}:outputs"

    redis_instance = method.__self__._redis

    inputs = redis_instance.lrange(inputs_key, 0, -1)
    outputs = redis_instance.lrange(outputs_key, 0, -1)

    print(f"{qualified_name} was called {len(inputs)} times:")

    for input_str, output_str in zip(inputs, outputs):
        print(f"{qualified_name}(*{input_str.decode('utf-8')}) -> {output_str.decode('utf-8')}")  # noqa
