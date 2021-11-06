from flask import Flask
import os

os.environ["FLASK_APP"] = "hello"

print(os.environ["FLASK_APP"])

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def hello_world():
    return "<p>Good bye, World!</p>"