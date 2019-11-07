from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/<int:pag>/<int:tam>/', methods=['GET'])
def index(pag=None, tam=None):
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

if __name__=="__main__":
    app.run(debug='True', host='0.0.0.0', port=5555)