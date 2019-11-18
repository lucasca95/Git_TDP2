from application import app, db
from flask import render_template, redirect

@app.route('/seeds')
def run_seeds():
    if (app.config['SEED_RAN'] == False):
        app.config['SEED_RAN'] = True
        # Inicializar BDD
        print('Se inicializa BDD y se cambia el valor app.config[SEED_RAN] a', app.config['SEED_RAN'])

    return redirect('/')