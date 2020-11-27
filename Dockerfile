FROM tiangolo/uwsgi-nginx-flask:python3.8

RUN pip install pipenv

ENV REQ_DIR /requirements

COPY Pipfile Pipfile.lock ${REQ_DIR}/

RUN cd ${REQ_DIR} && pipenv install --system --deploy

WORKDIR /app