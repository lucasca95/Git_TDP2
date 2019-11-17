from application import db
from datetime import datetime

# Modelo de ESP
class Esp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mac = db.Column(db.String(17))
    esp_version = db.Column(db.Integer, unique = False)
    created_at = db.Column(db.DateTime, default = datetime.now)
    updated_at = db.Column(db.DateTime, default = datetime.now)

    def __init__(self, mac, esp_version):
      self.mac = mac
      self.esp_version = esp_version