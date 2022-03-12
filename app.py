import os
from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)


def get_db():
    client = MongoClient(host=os.environ['MONGODB_HOSTNAME'],
                         port=27017,
                         username=os.environ['MONGODB_USERNAME'],
                         password=os.environ['MONGODB_PASSWORD'],
                         authSource=os.environ['MONGODB_DATABASE'])
    db = client[os.environ['MONGODB_DATABASE']]
    return db


@app.route('/')
def ping_server():
    return "Welcome to the world of animals."


@app.route('/animals')
def get_stored_animals():
    db = get_db()
    _animals = db.animal_tb.find()
    animals = [{"id": animal["id"], "name": animal["name"], "type": animal["type"]} for animal in _animals]
    return jsonify({"animals": animals})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
