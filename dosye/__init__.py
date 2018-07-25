# Import from standard library
from uuid import uuid4

# Import from flask
from flask import Flask
from flask_menu import Menu

# Import from dosye
from dosye.files import FilesManager

__version__ = '0.0.1'

UPLOAD_FOLDER = '/var/dosye/uploads'


class CustomFlask(Flask):
    """
    Override default Flask configuration for Jinja2 delimiters,
    in order to be compatible with VueJS delimiters.

    Flask Jinja2 delimiters: ${ ... }
    VueJS delimiters: {{ ... }}
    """
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update({
        'variable_start_string': '${',
        'variable_end_string': '}',
    })


app = CustomFlask(__name__)
app.config['FILES_MANAGER'] = FilesManager(UPLOAD_FOLDER)
app.secret_key = str(uuid4())

Menu(app=app)

import dosye.routes  # noqa: F401
