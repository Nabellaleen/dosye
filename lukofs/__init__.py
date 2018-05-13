from uuid import uuid4
from flask import Flask

__version__ = '0.0.1'

UPLOAD_FOLDER = '/var/lukofs/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = uuid4()

import lukofs.routes  # noqa: F401
