from flask import Flask, Response, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import re

# Init App
app = Flask(__name__)
# Establecer clave secreta para uso de variables de session en cookies
# y setearlas como permanentes
app.secret_key="1234"
@app.before_request
def session_management():
  session.permanent = True

basedir = os.path.abspath(os.path.dirname(__file__))
# BDD
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init SQLAlchemy
db = SQLAlchemy(app)
# Init Marshmallow
mw = Marshmallow(app)

# ---- CLASES ----
# Modelo de Dispositivo
class Dispositivo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mac = db.Column(db.String(17))
    act_firmware = db.Column(db.Integer, unique = False)

    def __init__(self, mac, act_firmware):
      self.mac = mac
      self.act_firmware = act_firmware

# ---- FIN CLASES ----

@app.route('/', methods=['GET'])
@app.route('/<int:pag>/<int:tam>/', methods=['GET'])
def index(pag=None, tam=None):
    session.clear()
    session["cantMAC"] = 0
    if ((pag==None) or (tam==None)):
        return "ERROR. Por favor elegir /pag/tam"
    else:
        #Leer el archivo
        f_name='chico.txt'
        try:
            f=open("./testFlask/programas/"+f_name, 'rt')
            contenido=f.readlines()
        except:
            print('Hubo un error en el try')
        finally:
            f.close()
        if ((pag==0)and(tam==0)):
            longitud=len(contenido)
            #Devolver todo el archivo
            s=''
            for lin in contenido:
                s += lin.strip()
            return render_template('index.html', param_contenido=s, param_longitud=longitud)
        elif (tam==0):
            return "Pedido de tam=0 invalido"
        elif (tam==1):
            #Devolver línea
            contenido=contenido[pag]
            longitud=1
            return render_template('index.html', param_contenido=contenido, param_longitud=longitud)
        else:
            #inicial = pag*tam
            #final = ((pag+1) * tam)
            contenido = contenido[(pag*tam):((pag+1)*tam)]
            longitud = len(contenido)
            s=''
            for lin in contenido:
                s += lin.strip()
            return render_template('index.html', param_contenido=s, param_longitud=longitud)
        return "ERROR EN LOS PARAMETROS"

@app.route('/grupo', methods=['GET'])
def creditos():
    return render_template('grupo.html')

@app.route('/<mac>', methods=['GET', 'POST'])
def check_version(mac=None):
    version = ''
    # Corroborar que no llegue MAC vacía
    if(mac == None):
        version= "Llega MAC vacía"
    # Corroborar formato de direcc MAC
    elif (re.match("^([0-f][0-f][:-]){5}[0-f][0-f]$", mac)):
        if (mac.upper() == 'A0:20:A6:00:F3:CD'):
            version = 'NewVersion'
        elif (mac.upper() == 'A0:20:A6:00:F3:CC'):
            version = 'Updated'
        elif (mac.upper() == 'TUVIEJAENTANGA'):
            version = 'Vaaamooo newelsss'
        else:
            version = 'Invalid'
    # El formato de MAC es inválido
    else:
        version = 'Formato de MAC inválido'
    return render_template('dar_version.html', param_version=version)

@app.route('/dispositivos/', methods=['GET', 'POST'])
def dispositivo_index():
    lista_dispositivos = Dispositivo.query.all()
    return render_template('./dispositivo/index.html', param_lista_dispositivos=lista_dispositivos)

@app.route('/dispositivos/create', methods=['GET', 'POST'])
def dispositivo_create():
    if request.method == 'GET':
        print("Entramos al GET")
        return render_template('./dispositivo/create.html')
    elif (request.method == 'POST'):
        nueva_mac='A0:BB:BB:BB:22:AA'
        if (session["cantMAC"] == 0):
            nueva_mac='A0:20:A6:00:F3:CD'
            session["cantMAC"] = 1
        elif (session["cantMAC"] == 1):
            nueva_mac='A0:20:A6:00:F3:CC'
            session["cantMAC"] = 2
        nuevo_dispositivo = Dispositivo(mac=nueva_mac,act_firmware=1)
        db.session.add(nuevo_dispositivo)
        db.session.commit()
        return redirect('/dispositivos/')

# Run Server
if __name__=="__main__":
    app.run(debug='True', host='0.0.0.0', port=5555)