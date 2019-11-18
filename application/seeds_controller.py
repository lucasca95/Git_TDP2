from application import app, db
from application.models.device import Device
from application.models.esp import Esp
from application.models.target import Target
from application.models.program import Program
from application.models.error import Error
from application.models.devicesprograms import devicesprograms

from flask import render_template, redirect

@app.route('/seeds')
def run_seeds():
    if (app.config['SEED_RAN'] == False):
        app.config['SEED_RAN'] = True

        ### Inicializar BDD ###
        # Devices
        dev1 = Device(device_name="Arduino UNO", device_latitude=0, device_longitude=0)
        # ESPs
        esp1 = Esp(mac='AA:BB:CC:DD:EE', esp_version=1)
        # Targets
        tar1 = Target(target_type=1)
        # Programs
        prog1 = Program(program_version=1, program_name='Blinky')
        # Errors
        err1 = Error(msg='Nos quedamo sin yerba')
        
        db.session.add(esp1)
        db.session.add(tar1)
        db.session.add(prog1)
        db.session.add(err1)
        db.session.commit()

        # Vincular objetos
        dev1.programs.append(prog1)
        dev1.esp_id = esp1.id   # NO ESTÁ FUNCIONANDO -- REVISAR!!!!
        dev1.target_id = tar1.id
        db.session.add(dev1)

        db.session.commit()

        print('Se inicializa BDD y se cambia el valor app.config[SEED_RAN] a', app.config['SEED_RAN'])

    return redirect('/')