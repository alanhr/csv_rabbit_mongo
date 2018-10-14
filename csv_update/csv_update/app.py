from flask import Flask, jsonify, request

from csv_update.DispatchFileUser import DispatchFileUser

app = Flask(__name__)


@app.route("/health")
def healthcheck():
    return jsonify({"status": "UP"}), 200


@app.route("/users/upload", methods=["POST"])
def upload():
    dispatch_file = DispatchFileUser(request.files)

    dispatch_file.send()

    if dispatch_file.successded():
        return '', 200

    return (jsonify({**dispatch_file.get_error(), 'status_code': 400}),
            400, {'ContentType': 'application/json'})
