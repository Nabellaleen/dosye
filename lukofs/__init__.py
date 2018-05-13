__version__ = '0.0.1'

from uuid import uuid4
from flask import Flask

UPLOAD_FOLDER = '/var/lukofs/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = uuid4()

import lukofs.routes
