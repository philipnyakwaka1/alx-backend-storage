#!/usr/bin/env python3
"""Script to provide some stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient

def get_logs_count(collection):
    """Returns the number of documents in the collection"""
    return collection.count_documents({})

def get_method_count(collection, method):
    """Returns the count of documents with the given method"""
    return collection.count_documents({'method': method})

def get_method_path_count(collection, method, path):
    """Returns the count of documents with the given method and path"""
    return collection.count_documents({'method': method, 'path': path})

def main():
    client = MongoClient()
    db = client.logs
    collection = db.nginx

    total_logs = get_logs_count(collection)
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = get_method_count(collection, method)
        print(f"\tmethod {method}: {count}")

    specific_count = get_method_path_count(collection, "GET", "/status")
    print(f"method=GET path=/status: {specific_count}")

if __name__ == "__main__":
    main()
