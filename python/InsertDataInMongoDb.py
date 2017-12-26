from pymongo import MongoClient

client = MongoClient('localhost',)

class TwitterStream:
    def dump_data(self):
        while True:
            db = client.Distributed
            db.insert({'some stuff': 'other stuff'})