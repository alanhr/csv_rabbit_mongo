from flask import Flask, jsonify, request

from csv_update.CsvToList import CsvToList
from csv_update.Queue import Queue
from csv_update.utils.file import save_tmp_file

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['csv'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/health")
def healthcheck():
    return jsonify({"status": "UP"}), 200


@app.route("/users/upload", methods=["POST"])
def upload():

    file = request.files.get('file')

    if file and allowed_file(file.filename):

        full_path_file = save_tmp_file(file)

        csvToList = CsvToList(
            open(full_path_file))

        users = csvToList.get_list()

        queue = Queue()

        queue.send_batch('user', users)

        queue.close()

        return '', 200

    return jsonify({'status_code': 400}), 400, {'ContentType': 'application/json'}
