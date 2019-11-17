from application import db
from datetime import datetime

# Modelo de 
class (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    = db.Column(db.Integer, unique = True)
    created_at = db.Column(db.DateTime, default = datetime.now)
    updated_at = db.Column(db.DateTime, default = datetime.now)

    def __init__(self, ):
      self. = 