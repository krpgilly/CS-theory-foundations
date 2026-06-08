from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)


@app.route("/inspect", methods=["GET", "POST", "PUT", "DELETE"])
def inspect():
    """
    A request inspector endpoint that returns raw request metadata.
    Demonstrates HTTP lifecycle, REST principles, and CORS behaviour.
    """

    data = {
        "method": request.method,
        "path": request.path,
        "remote_addr": request.remote_addr,
        "query_params": request.args.to_dict(),
        "json_body": request.get_json(silent=True),
        "form_data": request.form.to_dict(),
        "headers": dict(request.headers),
        "raw_body": request.data.decode("utf-8") if request.data else None,
    }

    return jsonify(data), 200


@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    app.run(debug=True)
