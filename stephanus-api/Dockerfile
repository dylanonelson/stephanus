FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

ENV PYTHON_ENV=production

CMD [ "gunicorn", "-b", "0.0.0.0:8080", "-k", "gevent", "--log-level", "debug", "app:app" ]
