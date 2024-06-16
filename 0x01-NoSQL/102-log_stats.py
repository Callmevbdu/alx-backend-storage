#!/usr/bin/env python3
"""
Improve 12-log_stats.py by adding the top 10 of the most present IPs in
the collection nginx of the database logs
"""
from pymongo import MongoClient


def log_stats(mongo_collection):
    """ Print log statistics, including the top 10 of the most present IPs. """
    top_ips = mongo_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    print("IPs:")
    for ip in top_ips:
        print(f"    {ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx

    log_stats(nginx_collection)
