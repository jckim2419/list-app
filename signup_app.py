# signup_app.py
from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
DB_FILE = '/data/db.json'

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'Missing name or email'}), 400

    if not os.path.exists(DB_FILE):
        users = []
    else:
        with open(DB_FILE, 'r') as f:
            users = json.load(f)

    users.append({'name': data['name'], 'email': data.get('email', '')})

    with open(DB_FILE, 'w') as f:
        json.dump(users, f)

    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
