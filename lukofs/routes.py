# Import from flask
from flask import render_template, redirect, url_for, request, flash

# Import from lukofs
from lukofs import app
from lukofs.files import FilesManagerException
from lukofs.upload import handle_upload_request


@app.route('/')
def index():
    return redirect(url_for('upload'))


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    elif request.method == 'POST':
        goto = handle_upload_request(request)
        return redirect(goto)


@app.route('/browse')
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
