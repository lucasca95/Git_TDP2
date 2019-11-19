from application import app
from flask import render_template
# operator: se usa para ordenar elementos de un diccionario
import operator

@app.route('/')
def index():
    print('El valor de app.config[SEED_RAN] es', app.config['SEED_RAN'])
    return render_template('./home/index.html')

@app.route('/about/')
def about():
    return render_template('./home/grupo.html')

@app.route('/config/')
def printConfig():
    config_list = sorted(app.config.items(), key=operator.itemgetter(0))
    return render_template('./home/printConfig.html', param_config_list=config_list)