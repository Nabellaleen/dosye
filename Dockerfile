FROM python:3.6

ENV SRC /dosye
ENV FLASK_APP dosye
ENV FLASK_RUN_PORT=5000

ADD . ${SRC}

WORKDIR ${SRC}

RUN pip3 install .

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
