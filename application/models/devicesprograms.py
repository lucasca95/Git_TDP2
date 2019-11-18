from application import db
from datetime import datetime

# Modelo de DevicesPrograms
devicesprograms = db.Table('devicesprograms', 
	db.Column('id', db.Integer, primary_key=True),
	db.Column('device_id', db.Integer, db.ForeignKey('device.id')),
	db.Column('program_id', db.Integer, db.ForeignKey('program.id')),
	db.Column('created_at', db.DateTime, default = datetime.now),
	db.Column('updated_at', db.DateTime, default = datetime.now)
)