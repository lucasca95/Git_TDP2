# Traer de la carpeta "app" el objeto "app"
from application import app

if(__name__ == '__main__'):
    app.run(debug=True, host = '0.0.0.0', port=5555)
