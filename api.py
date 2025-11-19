from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    code = request.json.get("code")
    return jsonify({"issues": []})

if __name__ == "__main__":
    app.run()
