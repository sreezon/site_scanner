#set FLASK_APP=C:\Users\Ali.000\Desktop\sitescanner\app.py
#set FLASK_ENV=development

from flask import Flask, request, jsonify, render_template
from ScannerService import ScannerService

app = Flask(__name__)
PORTS = '0-1000'
app.config['JSON_SORT_KEYS'] = False


scanner_service = ScannerService()


@app.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return render_template('form.html')


@app.post("/scan_page")
def scan_page():
    data = request.form['scan']
    sites = data.split()
    return scanner_service.scan_sites(sites)
    

