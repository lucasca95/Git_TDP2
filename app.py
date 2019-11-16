from flask import Flask, Response, render_template, request, redirect, url_for, session
from flaskext.mysql import MySQL
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

# BDD - MySQL
mysql = MySQL()
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Culosucio'
app.config['MYSQL_DATABASE_DB'] = 'cicd'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

# Conexión con BDD
conn = mysql.connect()
# Crear cursor
cursor = mysql.get_db().cursor()

# ---- CLASES ----
# Modelo de Dispositivo
class Esp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mac = db.Column(db.String(17))
    versionEsp = db.Column(db.Integer, unique = False)

    def __init__(self, mac, versionEsp):
      self.mac = mac
      self.versionEsp = versionEsp
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

@app.route('/<macEsp>', methods=['GET', 'POST'])
def check_version(macEsp=None):
    versionEsp = ''
    # Corroborar que no llegue MAC vacía
    if(macEsp == None):
        versionEsp= "Llega MAC vacía"
    # Corroborar formato de direcc MAC
    elif (re.match("^([0-f][0-f][:-]){5}[0-f][0-f]$", macEsp)):
        if (macEsp.upper() == 'A0:20:A6:00:F3:CD'):
            versionEsp = 'NewVersion'
        elif (macEsp.upper() == 'A0:20:A6:00:F3:CC'):
            versionEsp = 'Updated'
        elif (macEsp.upper() == 'TUVIEJAENTANGA'):
            versionEsp = 'Vaaamooo newelsss'
        else:
            versionEsp = 'Invalid'
    # El formato de MAC es inválido
    else:
        versionEsp = 'Formato de MAC inválido'
    return render_template('dar_version.html', param_versionEsp=versionEsp)

@app.route('/esps/', methods=['GET', 'POST'])
def esps_index():
    esp_list = Esp.query.all()
    return render_template('./esp/index.html', param_esp_list=esp_list)

@app.route('/esps/create', methods=['GET', 'POST'])
def dispositivo_create():
    if request.method == 'GET':
        print("Entramos al GET")
        return render_template('./esps/create.html')
    elif (request.method == 'POST'):
        new_mac='A0:BB:BB:BB:22:AA'
        if (session["cantMAC"] == 0):
            new_mac='A0:20:A6:00:F3:CD'
            session["cantMAC"] = 1
        elif (session["cantMAC"] == 1):
            new_mac='A0:20:A6:00:F3:CC'
            session["cantMAC"] = 2
        new_esp = Esp(mac=new_mac,versionEsp=1)
        db.session.add(new_esp)
        db.session.commit()
        return redirect('/esps/')

# Run Server
if __name__=="__main__":
    app.run(debug='True', host='0.0.0.0', port=5556)