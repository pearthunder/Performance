import os
import random
import time
from typing import Any

from flask import Flask, jsonify, request, make_response
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


# Deny all non-GET methods with HTTP 500
@app.before_request
def deny_non_get() -> Any:
	if request.method != "GET":
		return make_response(jsonify({"error": "internal server error"}), 500)


# Catch-all for any GET path: respond with fixed success after random delay (1-10s)
@app.route('/', defaults={'path': ''}, methods=["GET"]) 
@app.route('/<path:path>', methods=["GET"]) 
def catch_all_get(path: str) -> Any:
	delay_seconds = random.randint(1, 10)
	time.sleep(delay_seconds)
	return jsonify({
		"status": "success",
		"message": "OK",
		"delay_seconds": delay_seconds,
	}), 200


if __name__ == "__main__":
	port = int(os.environ.get("PORT", "5000"))
	host = os.environ.get("HOST", "0.0.0.0")
	app.run(host=host, port=port, debug=True)



