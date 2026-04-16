from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
# This specific configuration is required to stop "Bridge Retrying"
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/')
def home():
    return "SAVAGE SERVER ONLINE"

@app.route('/api/check', methods=['POST', 'OPTIONS'])
def check():
    if request.method == 'OPTIONS':
        return jsonify({"status": "ok"}), 200
        
    data = request.get_json()
    name = data.get("username")
    
    url = f"https://auth.roblox.com/v1/usernames/validate?username={name}&birthday=2004-10-10"
    
    try:
        r = requests.get(url, timeout=5)
        return jsonify(r.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def handler(request):
    return app(request)
