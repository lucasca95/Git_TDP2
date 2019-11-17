from application import db
from device import Device
from datetime import datetime

class Error(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    ## Atributos ##
    message = db.Column(db.String(200))

    ## Relaciones ##
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'))

    ## Hora ##
    created_at = db.Column(db.DateTime, default = datetime.now)
    updated_at = db.Column(db.DateTime, default = datetime.now)
    
    def __init__(self, msg):
        self.message = msg
