from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/api/check', methods=['POST'])
def check():
    name = request.json.get("username")
    url = f"https://auth.roblox.com/v1/usernames/validate?username={name}&birthday=2004-10-10"
    try:
        r = requests.get(url, timeout=5)
        return jsonify(r.json())
    except:
        return jsonify({"error": "Timeout"}), 500

def handler(request):
    return app(request)
