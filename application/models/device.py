from application import db
from .devicesprograms import devicesprograms
from datetime import datetime

# Modelo de Device
class Device(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  device_name = db.Column(db.String(50), unique = False)
  device_latitude = db.Column(db.Integer, unique = False)
  device_longitude = db.Column(db.Integer, unique = False)

  ### Relaciones ###
  # un device pertenece a una ESP
  esp_id = db.Column(db.Integer, db.ForeignKey('esp.id'))

  # tipo de target del dispositivo
  target_id = db.Column(db.Integer, db.ForeignKey('target.id'))

  # un device posee varios programs
  programs = db.relationship('Program', secondary=devicesprograms, backref=db.backref('devices', lazy='dynamic'))

  # un device puede tener muchos errores
  errors = db.relationship('Error', backref='device')

  ### Hora de creación y modificación ###
  created_at = db.Column(db.DateTime, default = datetime.now)
  updated_at = db.Column(db.DateTime, default = datetime.now)

  def __init__(self, device_name, device_latitude, device_longitude):
    self.device_name = device_name
    self.device_latitude = device_latitude
    self.device_longitude = device_longitude