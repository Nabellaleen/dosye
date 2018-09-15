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

You should create manually the /var/dosye/uploads directory and attribute correctly the rights.

    sudo mkdir -p /var/dosye/uploads
    sudo chown -R $USER:$USER /var/dosye

### Virtualenv

You should setup a virtual environment to keep dosye dependancies
independant of your system.

If you're not familiar with virtual environments, here are instructions to use pew or pipenv, which are both a tool to manage virtual environnements easily. Feel free to choose one and follow the given explanations.

#### pew 
    
To install pew, check https://pypi.org/project/pew/

Then checkout the project and create the virtualenv :

    git clone https://github.com/bepatient-fr/dosye.git
    cd dosye
    pew new --python python3 dosye
    pew setproject .

To activate the virtualenv :

    pew workon dosye

After activation, any python command is executed in this virtual environnementm isolated from the operating system (python, pip, ...).

To leave the virtualenv, use `ctrl-D` or `exit`.

#### pipenv

To install pipenv, check https://pipenv.readthedocs.io/en/latest/

Then checkout the project and create the virtualenv :

    git clone https://github.com/bepatient-fr/dosye.git
    cd dosye
    pipenv --python python3

To activate the virtualenv :

    cd dosye
    pipenv shell

After activation, any python command is executed in this virtual environnementm isolated from the operating system (python, pip, ...).

To leave the virtualenv, use `ctrl-D` or `exit`.

### Installation

With the virtualenv activated, follow these steps :

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