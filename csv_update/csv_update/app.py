import os
from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename
from tempfile import gettempdir
from csv_update.CsvToList import CsvToList

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['csv'])
app.config['UPLOAD_FOLDER'] = gettempdir()


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/health")
def healthcheck():
    return jsonify({"status": "UP"}), 200

@app.route("/upload",methods=["POST"])
def upload():
    if 'file' not in request.files:
        return jsonify({'status_code': 400}),400
    
    file = request.files['file']

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        csvToList = CsvToList(
            open(os.path.join(app.config['UPLOAD_FOLDER'], filename)))

        listDict = csvToList.get_list()

        return jsonify({'body':listDict}),200
