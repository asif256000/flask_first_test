FROM python:slim

RUN useradd flasktest

WORKDIR /home/flasktest

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn pymysql cryptography

COPY app_pkg app_pkg
COPY migrations migrations
COPY microblog.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP microblog.py

RUN chown -R flasktest:flasktest ./
USER flasktest

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
