# Import from flask
from flask import flash, url_for

# Import from dosye
from dosye import app
from dosye.files import FilesManagerException


def handle_upload_request(request):
    if 'file' not in request.files:
        flash('Select a file before trying to upload it', 'error')
        return request.url
    file = request.files['file']
    if file.filename == '':
        flash('Select a file before trying to upload it', 'error')
        return request.url

    files_manager = app.config['FILES_MANAGER']
    try:
        file_name = files_manager.save(file)
    except FilesManagerException as e:
        flash(e.message, 'error')
        return request.url

    flash(f"File sucessfully uploaded: {file_name}", 'success')
    return url_for('upload')
