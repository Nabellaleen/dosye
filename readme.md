Luko File Server
================

A little webserver to store and manage some files

Docker - The easy way
---------------------

### Docker Compose

Default targeted folder is defined in .env file and can be overrided by LUKOFS_UPLOADS_PATH
environment variable

    git clone https://github.com/Nabellaleen/lukofs.git
    cd lukofs
    docker-compose up --build -d

Then navigate to http://localhost:5000

### Docker

Default targeted folder is defined by the -v docker parameter

    git clone https://github.com/Nabellaleen/lukofs.git
    cd lukofs
    docker build -t lukofs:latest .
    docker run -d -p 5000:5000 -v /var/lukofs/uploads:/var/lukofs/uploads lukofs:latest

Then navigate to http://localhost:5000

Production
----------

### Installation

    git clone https://github.com/Nabellaleen/lukofs.git
    cd lukofs
    pip install .

### Usage

    lukofs

Development
-----------

For development, sources are symlinked to site-packages and
flask is launched in debug mode, which enable traceback reports
and live reload from sources.

You should create manually the /var/lukofs/uploads directory.

### Installation

    git clone https://github.com/Nabellaleen/lukofs.git
    cd lukofs
    pip install -r requirements-dev.txt
    pip install -e .
    export FLASK_APP=lukofs
    export FLASK_ENV=development

### Usage

    flask run

### Quality

Ensure code conventions by using flake8:

    flake8