from flask import Flask
from flask import render_template

import RPi.GPIO as GPIO
import time

app = Flask(__name__)

@app.route('/led/enlazar')
def enlazar():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(19, GPIO.OUT) ## GPIO 19 como salida
    return "true"

@app.route('/led/desenlazar')
def desenlazar():
    GPIO.cleanup()
    return "false"

@app.route("/led/encender")
def encender():
     GPIO.output(19, True)
     return "encendido"

@app.route("/led/apagar")
def apagar():
    GPIO.output(19, False)
    return "apagado"


@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0') 
