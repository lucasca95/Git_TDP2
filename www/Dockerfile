#Dockerfile es el archivo que va a configurar qué elementos tiene y qué
#se instala en un contenedor docker

#Imagen base de SO
#En este caso la imagen base es python y con los ":" especificamos la versión
FROM python:3.6.6-alpine3.8

ENV FLASK_APP app.py
ENV FLASK_DEBUG 1
ENV FLASK_RUN_PORT 8888

#RUN se usa para dar las instrucciones que deben ejecutarse al momento
#de construir la imagen
RUN apk add bash gcc musl-dev mysql mariadb-dev
RUN mkdir /www/
ADD requeriments.txt /www/requeriments.txt
RUN pip install -r /www/requeriments.txt 

EXPOSE 8888

WORKDIR /www/
ENTRYPOINT [ "python", "-m", "flask", "run", "--host=0.0.0.0" ]