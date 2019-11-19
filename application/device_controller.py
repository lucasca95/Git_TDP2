from application import app
from application.models.device import Device
from flask import render_template

@app.route('/devices/', methods=['GET'])
def device_index():
    devices_list = Device.query.all()
    return render_template('./device/index.html', param_devices_list=devices_list)