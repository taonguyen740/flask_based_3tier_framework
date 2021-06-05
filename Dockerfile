FROM tiangolo/uwsgi-nginx-flask:python3.7
LABEL maintainer="Dinh Tao <dinhtao995@gmail.com>"

# -- Set TimeZone to JP
RUN rm /etc/localtime \
    && echo Asia/Tokyo > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata

ARG DB_HOST
ARG DB_PORT
ARG DB_NAME
ARG DB_USERNAME
ARG DB_PASSWORD

ENV DB_HOST $DB_HOST
ENV DB_PORT $DB_PORT
ENV DB_NAME $DB_NAME
ENV DB_USERNAME $DB_USERNAME
ENV DB_PASSWORD $DB_PASSWORD
# -- Adding Pipfiles
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
# -- Install dependencies:
RUN set -ex && pipenv install --deploy --system
# Add app
COPY ./src /app/src
COPY uwsgi.ini /app
COPY nginx.timeout.conf /etc/nginx/conf.d/
COPY nginx.proxy.conf /etc/nginx/conf.d/
RUN chmod +x prestart.sh