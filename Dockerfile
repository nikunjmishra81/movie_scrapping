FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED 1
COPY deployment/requirements.txt /
RUN pip install -r /requirements.txt
WORKDIR /app/src
COPY ./src /app/src
ENV PYTHONPATH /app
RUN python manage.py db init
RUN python manage.py db migrate
RUN python manage.py db upgrade


EXPOSE 5000

#CMD ["gunicorn", "-b", "0.0.0.0:5000", "-w", "4", "src.app:app"]
