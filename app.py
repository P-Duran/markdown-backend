from flask import Flask

from controller.markdown_controller import markdown_controller
from controller.page_controller import page_controller
from controller.user_controller import user_controller

app = Flask(__name__)
app.secret_key = "testing"
app.register_blueprint(markdown_controller)
app.register_blueprint(user_controller)
app.register_blueprint(page_controller)


@app.route('/')
def ping_server():
    return "The server is running smoothly"


@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Methods']='*'
    response.headers['Access-Control-Allow-Origin']='*'
    response.headers['Access-Control-Allow-Headers']='*'
    response.headers['Vary']='Origin'
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
