from flask import Flask, request, jsonify
from config import SAMPLE_CONST
import json
import base64

app = Flask(__name__)


def decode_client_principal(val):
    decoded_bytes = base64.b64decode(val)

    decoded_str = decoded_bytes.decode("utf-8")

    user_info = json.loads(decoded_str)
    return user_info


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
def bye_world():
    return "<p>Bye, World!</p>"


@app.route("/const")
def const():
    return f"<p>CONST={SAMPLE_CONST}!</p>"


@app.route("/get-user-info", methods=['GET'])
def get_user_info():
    principal = request.headers.get('x-ms-client-principal')

    if not principal:
        return jsonify({"error": "x-ms-client-principal not found"}), 400

    try:
        print(f"x-ms-client-principal: {principal}")

        user_info = decode_client_principal(principal)

        return jsonify(user_info), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
