from flask import Flask

from controller.markdown_controller import markdown_controller

app = Flask(__name__)

app.register_blueprint(markdown_controller)

@app.route('/')
def ping_server():
    return "The server is running smoothly"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
