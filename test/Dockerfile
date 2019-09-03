#Dockerfile

FROM python:3.6.6-alpine3.8

ENV FLASK_APP app.py
ENV FLASK_DEBUG 1
ENV FLASK_RUN_PORT 8888

#Copiar todo lo que esté en nuestra carpeta actual (lo indicamos con ".")
#a la carpeta /app dentro del contenedor Docker
COPY . /app

#indica a Docker que nuestro directorio de trabajo es justamente /app
WORKDIR /app

#Mediante el comando pip instala los módulos que especifiquemos en el archivo
#requirements.txt (uno x cada linea)
RUN pip install -r requirements.txt

EXPOSE 8888

#Ejecutamos, estando parados en /app, el la línea "python app.py"
###ENTRYPOINT ["python"]
###CMD ["app.py"]
ENTRYPOINT [ "python", "-m", "flask", "run", "--host=0.0.0.0" ]
