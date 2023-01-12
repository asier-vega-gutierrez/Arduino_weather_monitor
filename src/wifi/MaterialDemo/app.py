from flask import Response, Flask, request
import serial
import time

app = Flask(__name__)
#ser = serial.Serial("COM3", 9800, timeout = 1)
#time.sleep(2)

@app.route("/", methods=['GET'])
def hello():
    while True:
        #line = ser.readline().decode()
        #print(type(line))
        #if len(line) < 15:
        #    valor = "1,0,0,0,0,0,0"
        #else:
        #    valor = line

        return "1,2,3,4,5,6,7,8" 

#flask run --host=0.0.0.0
#desde un directorio con app.py