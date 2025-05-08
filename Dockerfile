FROM apache/airflow:2.9.2-python3.10

USER root
COPY requirements.txt /requirements.txt

RUN pip install --upgrade pip && \
    pip install -r /requirements.txt

USER airflow
