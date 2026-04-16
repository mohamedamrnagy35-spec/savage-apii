from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
# This is the "Magic Line" that fixes the Bridge Retrying error
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def home():
    return "SAVAGE ENGINE ONLINE"

@app.route('/api/check', methods=['POST', 'OPTIONS'])
def check():
    if request.method == 'OPTIONS':
        return '', 200
    
    data = request.get_json()
    name = data.get("username")
    url = f"https://auth.roblox.com/v1/usernames/validate?username={name}&birthday=2004-10-10"
    
    try:
        r = requests.get(url, timeout=5)
        return jsonify(r.json())
    except:
        return jsonify({"error": "timeout"}), 500

def handler(request):
    return app(request)
