
FROM osgeo/gdal:ubuntu-full-latest

ENV APP_ROOT /src
ENV CONFIG_ROOT /config

RUN mkdir ${CONFIG_ROOT}
COPY requirements.txt ${CONFIG_ROOT}/requirements.txt
RUN pip3 install -r ${CONFIG_ROOT}/requirements.txt

RUN mkdir ${APP_ROOT}
WORKDIR ${APP_ROOT}

ADD / ${APP_ROOT}
ENTRYPOINT ["./gunicorn_starter.sh"]