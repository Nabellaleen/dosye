DOSYE - File Server
===================

A little webserver in Python3 to store and manage some files

Docker - The easy way
---------------------

### Docker Compose

Default targeted folder is defined in .env file and can be overrided by DOSYE_UPLOADS_PATH
environment variable

    git clone https://github.com/bepatient-fr/dosye.git
    cd dosye
    docker-compose up --build -d

Then navigate to http://localhost:5000

### Docker

Default targeted folder is defined by the -v docker parameter

    git clone https://github.com/bepatient-fr/dosye.git
    cd dosye
    docker build -t dosye:latest .
    docker run -d -p 5000:5000 -v /var/dosye/uploads:/var/dosye/uploads dosye:latest

Then navigate to http://localhost:5000

Production
----------

### Installation

    git clone https://github.com/bepatient-fr/dosye.git
    cd dosye
    pip install .

### Usage

    dosye

Development
-----------

For development, sources are symlinked to site-packages and
flask is launched in debug mode, which enable traceback reports
and live reload from sources.

You should create manually the /var/dosye/uploads directory.

### Virtualenv

You should setup a virtual environment to keep dosye dependancies 
independant of your system.

#### pew

    git clone https://github.com/bepatient-fr/dosye.git
    cd dosye
    pew new --python python3 dosye
    pew setproject .

### Installation

    git clone https://github.com/bepatient-fr/dosye.git
    cd dosye
    pip install -r requirements-dev.txt
    pip install -e .
    export FLASK_APP=dosye
    export FLASK_ENV=development

### Usage

    flask run

### Quality

Ensure code conventions by using flake8:

    flake8