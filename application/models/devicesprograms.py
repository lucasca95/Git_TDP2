from application import db
from device import Device
from program import Program
from datetime import datetime

# Modelo de DevicesPrograms
class DevicesPrograms(db.Model):
	id = db.Column(db.Integer, primary_key=True)

	## Relaciones ##
	device_id = db.Column(db.Integer, db.ForeignKey('device.device_id'))
	program_id = db.Column(db.Integer, db.ForeignKey('program.program_id'))

	created_at = db.Column(db.DateTime, default = datetime.now)
	updated_at = db.Column(db.DateTime, default = datetime.now)
