from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET", "POST", "PUT", "DELETE"])
def test_route():
    s = f"\nMethod: {request.method}\n"
    s += f"Headers: {request.headers}\n"
    s += f"Parameters: {request.args}\n"
    s += f"Data: {request.get_json()}\n"
    print(s)
    return jsonify(dict(
        method=request.method,
        headers=dict(request.headers),
        parameters=request.args,
        data=request.get_json()
    ))


if __name__ == "__main__":
    app.run()
