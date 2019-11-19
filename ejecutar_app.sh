#!/bin/bash

export FLASK_APP=run.py
echo "Se carga FLASK_APP con valor $FLASK_APP"
export FLASK_ENV=development
echo "Se carga FLASK_ENV con valor $FLASK_ENV"

echo "Se ejecuta la aplicación Flask en host=localhost y puerto=5555"
flask run -h "0.0.0.0" -p 5555

