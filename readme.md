Luko File Server
================

A little webserver to store and manage some files

Production
----------

### Installation

    cd lukofs/
    pip install .

### Usage

    lukofs

Development
-----------

For development, sources are symlinked to site-packages and
flask is launched in debug mode, which enable traceback reports
and live reload from sources.

### Installation

    cd lukofs/
    pip install -e .
    export FLASK_APP=lukofs
    export FLASK_ENV=development

### Usage

    flask run
