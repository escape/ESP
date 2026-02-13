"""
Minimal registry service skeleton.
Serves machine-readable political influence data.
To be developed: data models, storage, and APIs.
"""

from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy", "service": "registry"}), 200

@app.route('/data', methods=['GET'])
def data():
    return jsonify({
        "message": "Registry service running",
        "status": "skeleton",
        "version": "0.1.0",
        "info": "Machine-readable political influence data endpoint"
    }), 200

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=True)
