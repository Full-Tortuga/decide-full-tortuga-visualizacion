from python:3.8.12-alpine3.15

RUN apk add --no-cache git postgresql-dev gcc libc-dev
RUN apk add --no-cache gcc g++ make libffi-dev python3-dev build-base

RUN pip install gunicorn
RUN pip install psycopg2
RUN pip install ipdb
RUN pip install ipython
RUN pip install pymongo[srv]


WORKDIR /app

RUN git clone https://github.com/Full-Tortuga/decide-full-tortuga-visualizacion.git .
RUN pip install -r requirements.txt



WORKDIR /app/decide

# local settings.py
ADD docker-settings.py /app/decide/local_settings.py


#Telegram token
ADD .env /app/decide/.env

RUN ./manage.py collectstatic

#CMD ["gunicorn", "-w 5", "decide.wsgi", "--timeout=500", "-b 0.0.0.0:5000"]
