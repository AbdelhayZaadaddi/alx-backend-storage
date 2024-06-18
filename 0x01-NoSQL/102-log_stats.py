#!/usr/bin/env python3
""" File 102-log_stats """

from pymongo import MongoClient


def log_stats(nginx_collection):
    """
        Python script that provides some
        stats about Nginx logs stored in MongoDB
    """

    print("{} logs".format(nginx_collection.count_documents({})))
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count_method = nginx_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count_method))
    path_status = nginx_collection.count_documents({"path": "/status"})
    print("{} status check".format(path_status))

    top_ips = nginx_collection.aggregate([
        {"$group":
            {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
         },
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {
            "_id": 0,
            "ip": "$_id",
            "count": 1
        }}
    ])

    print("IPs:")
    for top_ip in top_ips:
        ip = top_ip.get("ip")
        count = top_ip.get("count")
        print(f'\t{ip}: {count}')


def connected_to_mongo():
    """ Connects to MongoDB """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    log_stats(nginx_collection)


if __name__ == "__main__":
    connected_to_mongo()
