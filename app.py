from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index(pag=None, tam=None):
    if ((pag==None) or (tam==None)):
        return "ERROR. Por favor elegir /pag/tam"
    else:
        #Leer el archivo

        if ((pag==0) and (tam==0)):
            #Devolver todo el archivo
            pass
        elif (pag==tam):
            #Devolver sólo una línea
            pass
        return "Se devolvió una línea"

if __name__=="__main__":
    app.run(debug='True', host='0.0.0.0', port=5555)