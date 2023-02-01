FROM python:3.10.9
LABEL 'MAINTAINER' = 'Oleg V. Ivantsov, email: o.v.ivantsov@gmail.com'

COPY python/requirements.txt /requirements.txt

RUN apt-get update -y && apt-get install -y \
  libatlas-base-dev \
  gfortran \
  python-dev \
  nginx \
  tzdata \
  cron \
  zip \
  unzip \
  nano \
  vim

RUN python -m pip install --upgrade pip && pip install -r /requirements.txt

RUN useradd --no-create-home nginx
RUN rm /etc/nginx/sites-enabled/default
RUN rm -r /root/.cache

COPY nginx/nginx.conf /etc/nginx/
COPY nginx/site-config.conf /etc/nginx/conf.d/
COPY nginx/uwsgi.ini /etc/uwsgi/
COPY supervisord/supervisord.conf /etc/supervisord/
CMD supervisord -c /etc/supervisord/supervisord.conf