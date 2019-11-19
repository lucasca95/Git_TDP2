from application import app
from application.models.esp import Esp
from flask import render_template

@app.route('/esps/', methods=['GET'])
def esp_index():
    esps_list = Esp.query.all()
    return render_template('./esp/index.html', param_esps_list=esps_list)