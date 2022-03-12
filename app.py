import os
from flask import Flask, jsonify, request
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
    return "The server is running smoothly"

@app.route('/markdown')
def get_all_markdown():
    db = get_db()
    result = [{"text": markdown["text"]} for markdown in db.markdown.find()]
    return jsonify(result)

@app.route('/markdown/<id>')
def get_markdown_by_id(id):
    db = get_db()
    result = [{"text": markdown["text"]} for markdown in db.markdown.find({"_id": id})]
    return jsonify(result)

@app.route('/markdown', methods = ["POST"])
def post_markdown():
    db = get_db()
    db.markdown.insert_one({"text": request.form.get('text')})
    return jsonify({"text": request.form.get('text')})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
