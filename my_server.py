from flask import Flask, jsonify, request

app = Flask(__name__)  # instance of Flask variable, interface

@app.route("/", methods=["GET"])
def status():
    return "Server On"


@app.route("/info", methods=["GET"])
def info():
    return_dictionary = {
        "Author": "Claire Dong",
        "Version": "v1.0",
        "Data": [1.5, 26, 2]
        }
    return jsonify(return_dictionary)


@app.route("/sum", methods=["POST"])
def add():
    in_data = request.get_json()
    a = in_data["a"]
    b = in_data["b"]
    c = a + b
    return jsonify(c)


@app.route("/hello/<name>", methods=["GET"])
def say_hello(name):
    return "Hello, {}".format(name)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
