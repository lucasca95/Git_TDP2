from application import db
from datetime import datetime

# Modelo de Program
class Program(db.Model):
  id = db.Column(db.Integer, primary_key=True)

  ## Atributos ##
  program_version = db.Column(db.Integer, unique = False)
  program_name = db.Column(db.String(50), unique = False)

  ## Relaciones ##
  # un device tiene muchos programas
  # RELACION YA RESUELTA EN EL MODELO DEVICE Y DEVICESPROGRAMS

  created_at = db.Column(db.DateTime, default = datetime.now)
  updated_at = db.Column(db.DateTime, default = datetime.now)

  def __init__(self, program_version, program_name):
    self.program_version = program_version
    self.program_name = program_name