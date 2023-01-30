FROM python:3.10.9
LABEL 'MAINTAINER' = 'Oleg V. Ivantsov' 'EMAIL' = 'o.v.ivantsov@gmail.com'

COPY python/requirements.txt /requirements.txt

RUN apt-get update -y && apt-get install -y \
  python-dev \
  tzdata \
  cron \
  zip \
  unzip \
  nano \
  vim

RUN python -m pip install --upgrade pip && pip install \
  virtualenv \
  pandas \
  supervisor \
  sqlalchemy \
  psycopg2

#RUN pip install -r /requirements.txt
COPY supervisord/supervisord.conf /etc/supervisord.conf
CMD supervisord -c /etc/supervisord.conf