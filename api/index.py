from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app) # This fixes the connection errors you saw earlier

@app.route('/')
def home():
    return "Savage Engine is Online!"

@app.route('/api/check', methods=['POST'])
def check():
    name = request.json.get("username")
    # This is the official Roblox validation endpoint
    url = f"https://auth.roblox.com/v1/usernames/validate?username={name}&birthday=2004-10-10"
    try:
        r = requests.get(url, timeout=5)
        return jsonify(r.json())
    except:
        return jsonify({"error": "Roblox API Timeout"}), 500

# Required for Vercel to recognize the app
def handler(request):
    return app(request)
