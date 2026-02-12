from flask import Flask, jsonify, request

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return "Hello from Flask!"

# API route
@app.route("/api", methods=["GET"])
def api():
    return jsonify({
        "message": "This is a Flask API",
        "method": "GET"
    })

# POST example
@app.route("/data", methods=["POST"])
def receive_data():
    data = request.json
    return jsonify({
        "received": data
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
