from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
# This line allows the HTML tool to talk to the Vercel server
CORS(app, resources={r"/*": {"origins": "*"}}) 

@app.route('/api/check', methods=['POST', 'OPTIONS'])
def check():
    if request.method == 'OPTIONS':
        return '', 200
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
