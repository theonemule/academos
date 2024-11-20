# app.py
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

DAPR_STATE_URL = "http://localhost:3500/v1.0/state/statestore"

@app.route('/set', methods=['POST'])
def set_number():
    data = request.json
    state = [{
        "key": "number",
        "value": data['number']
    }]
    response = requests.post(DAPR_STATE_URL, json=state)
    return response.text, response.status_code

@app.route('/get', methods=['GET'])
def get_number():
    response = requests.get(f"{DAPR_STATE_URL}/number")
    if response.status_code == 200:
        return jsonify(response.json()), 200
    return response.text, response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)