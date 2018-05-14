# Import from flask
from flask import flash, jsonify, send_from_directory
from flask import render_template, redirect, url_for, request
from flask_menu import register_menu

# Import from lukofs
from lukofs import app
from lukofs.files import FilesManagerException
from lukofs.upload import handle_upload_request


@app.route('/')
def index():
    return redirect(url_for('upload'))


@app.route('/upload', methods=['GET', 'POST'])
@register_menu(app, '.upload', 'Upload a file')
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    elif request.method == 'POST':
        goto = handle_upload_request(request)
        return redirect(goto)


@app.route('/browse')
@register_menu(app, '.browse', 'Browse files')
def browse():
    file_manager = app.config['FILES_MANAGER']
    try:
        files = file_manager.get_files()
    except FilesManagerException as e:
        flash(e.message, 'error')
        files = []

    files_ns = []
    for i, file in enumerate(files):
        files_ns.append({
            'id': i,
            'filename': str(file.name),
        })
    return render_template('browse.html', files=files_ns)


@app.route('/delete/<filename>')
def delete_file(filename):
    try:
        file_manager = app.config['FILES_MANAGER']
        file_manager.delete(filename)
        return jsonify({
            'status': 'success',
            'filename': filename,
        })
    except FilesManagerException as e:
        return jsonify({
            'status': 'error',
            'error': e.message,
        })
    except BaseException as e:
        return jsonify({
            'status': 'error',
            'error': 'Unknown error',
            'exception': str(e),
        })


@app.route('/download/<filename>')
def download_file(filename):
    file_manager = app.config['FILES_MANAGER']
    if filename not in file_manager:
        flash(f'File not found: {filename}', 'error')
        return redirect(url_for('browse'))
    return send_from_directory(
        file_manager.folder, filename,
        as_attachment=True, attachment_filename=filename)
