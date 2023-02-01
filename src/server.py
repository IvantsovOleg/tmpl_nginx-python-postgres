from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/ping")
def ping():
    return "pong"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
