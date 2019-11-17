from application import db
from device import Device
from datetime import datetime

# Modelo de Target
class Target(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    ### Atributos ###
    target_type = db.Column(db.Integer, unique = True)

    ### Relaciones ###
    # dispositivos que son de este tipo de target
    devices = db.relationship('Device', backref='target')

    ###
    created_at = db.Column(db.DateTime, default = datetime.now)
    updated_at = db.Column(db.DateTime, default = datetime.now)

    def __init__(self, target_type):
      self.target_type = target_type