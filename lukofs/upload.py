# Import from standard library
import os

# Import from flask
from flask import flash, url_for
from werkzeug.utils import secure_filename


def handle_upload_request(request, folder):
    if 'file' not in request.files:
        flash('Select a file before trying to upload it', 'error')
        return request.url
    file = request.files['file']
    if file.filename == '':
        flash('Select a file before trying to upload it', 'error')
        return request.url
    filename = secure_filename(file.filename)
    try:
        file.save(os.path.join(folder, filename))
    except FileNotFoundError:
        flash("Error while saving the file - Please check "
              "server configuration: UPLOAD_FOLDER must "
              "exists and have correct rights", 'error')
        return request.url
    flash(f"File sucessfully uploaded: {filename}", 'success')
    return url_for('upload')
