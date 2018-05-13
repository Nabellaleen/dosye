# Import from flask
from flask import render_template, redirect, url_for, request

# Import from lukofs
from lukofs import app
from lukofs.upload import handle_upload_request


@app.route('/')
def index():
    return redirect(url_for('upload'))


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    elif request.method == 'POST':
        goto = handle_upload_request(request, app.config['UPLOAD_FOLDER'])
        return redirect(goto)
