from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from application.models import esp, target, program

app = Flask(__name__)

# Elegir el tipo de configuración acorde al entorno
# en el que se trabaje
if app.config['ENV'] == 'development':
    # Entrar al archivo "config" y levantar la configuración del objeto "DevelopmentConfig"
    app.config.from_object('config.DevelopmentConfig')
elif app.config['ENV'] == 'testing':
    app.config.from_object('config.TestingConfig')
else:
    app.config.from_object('config.ProductionConfig')

# BDD - MySQL
db = SQLAlchemy(app)

# from application import nombre_vista
from application import home_controller

### Listar los atributos de configuración ###
# for k,v in app.config.items():
#     print(k, str(v))

