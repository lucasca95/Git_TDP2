from application import app
from flask import render_template

@app.route('/')
def index():
    print('El valor de app.config[SEED_RAN] es', app.config['SEED_RAN'])
    return render_template('./home/index.html')

@app.route('/about')
def about():
    return render_template('./home/grupo.html')