from application import app
from application.models.error import Error
from flask import render_template

@app.route('/errors/', methods=['GET'])
def error_index():
    errors_list = Error.query.all()
    # Tomar los errores
    return render_template('./error/index.html', param_errors_list=errors_list)