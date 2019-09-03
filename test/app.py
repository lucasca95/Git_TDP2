# app.py - a minimal flask api
from flask import Flask
from flask import render_template

app = Flask(__name__)

#con el decorador "route" indicamos qué ruta del navegador disparará la ejecución
#del método puesto a continuación
@app.route('/')
def index():
    return render_template('index.html')

if __name__=="__main__":
    #Define HOST and PORT
        app.run(host='0.0.0.0', port=8888)
