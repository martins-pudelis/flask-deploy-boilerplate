from flask import Flask
from config import SAMPLE_CONST

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
def bye_world():
    return "<p>Bye, World!</p>"


@app.route("/const")
def const():
    return f"<p>CONST={SAMPLE_CONST}!</p>"