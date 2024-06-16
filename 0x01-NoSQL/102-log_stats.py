#!/usr/bin/env python3
"""
Improve 12-log_stats.py by adding the top 10 of the most present IPs in
the collection nginx of the database logs
"""
from pymongo import MongoClient


def display_nginx_log_summary(nginx_logs):
    '''Displays summary statistics of Nginx access logs.
    '''
    total_log_entries = nginx_logs.count_documents({})
    print(f'{total_log_entries} logs')
    print('Methods:')
    http_methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in http_methods:
        method_count = nginx_logs.count_documents({'method': method})
        print(f'\tmethod {method}: {method_count}')
    get_status_count = nginx_logs.count_documents({'method': 'GET', 'path': '/status'})  # noqa
    print(f'{get_status_count} status check')


def display_most_frequent_ips(log_collection):
    '''Displays the most frequent visitor IPs in the log collection.
    '''
    print('IPs:')
    ip_summary = log_collection.aggregate([
        {
            '$group': {'_id': '$ip', 'request_count': {'$sum': 1}}
        },
        {
            '$sort': {'request_count': -1}
        },
        {
            '$limit': 10
        }
    ])
    for entry in ip_summary:
        print(f'\t{entry["_id"]}: {entry["request_count"]}')


def main():
    '''Runs the log statistics display functions.
    '''
    mongo_client = MongoClient('mongodb://localhost:27017')
    nginx_log_collection = mongo_client.logs.nginx
    display_nginx_log_summary(nginx_log_collection)
    display_most_frequent_ips(nginx_log_collection)


if __name__ == '__main__':
    main()
