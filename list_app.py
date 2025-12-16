# list_app.py
from flask import Flask
import os
import json

app = Flask(__name__)
DB_FILE = '/data/db.json'

@app.route('/users')
def users():
    if not os.path.exists(DB_FILE):
        return json.dumps([]), 200

    with open(DB_FILE, 'r') as f:
        data = f.read()

    return data, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
