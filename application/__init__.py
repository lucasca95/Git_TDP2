from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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

# BDD
db = SQLAlchemy(app)
app.config['SEED_RAN'] = False

from application.models import device, program, error, esp, target, devicesprograms

# from application import xxxxx_controller
from application import home_controller

from application import device_controller
from application import error_controller
from application import esp_controller
from application import program_controller
from application import target_controller

from application import seeds_controller

### Listar los atributos de configuración ###
# for k,v in app.config.items():
#     print(k, str(v))

