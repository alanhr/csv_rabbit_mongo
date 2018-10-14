import os
from werkzeug.utils import secure_filename
from tempfile import gettempdir


def save_tmp_file(file):
    filename = secure_filename(file.filename)
    full_path_file = os.path.join(gettempdir(), filename)

    file.save(full_path_file)

    return full_path_file


def allowed_file(filename, types):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in set(types)
