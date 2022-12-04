from flask import Response, Flask, request
import prometheus_client
from prometheus_client.core import CollectorRegistry
from prometheus_client import Summary, Counter, Histogram, Gauge
import time
import random




app = Flask(__name__)

#Metrics to measure
graphs = {}
graphs['temp'] = Gauge('temperature_in_celsius', 'Temperature in Celsius')
graphs['press'] = Gauge('atmospheric_pressure', 'Atmostpheric Pressure')
graphs['hum'] = Gauge('humidity', 'Percentage of Humidity')
graphs['w_speed'] = Gauge('wind_speed', 'The speed of the wind in m/s')
graphs['w_dir'] = Gauge('wind_direction', 'The direction of the wind in degrees')
graphs['rain'] = Gauge('Rain_precipitation', 'Rain precipitations in l/m^2')


#Inicialization of applicaton where we set the metrics
@app.route("/", methods=['GET'])
def hello():
    #graphs['valor'].set(random.randrange(16000, 16150, 1))
    graphs['temp'].set(random.random())
    graphs['press'].set(random.random())
    graphs['hum'].set(random.random())
    graphs['w_speed'].set(random.random())
    graphs['w_dir'].set(random.random())
    graphs['rain'].set(random.random())
    return "Hello World!" 

#Get Metrics
@app.route("/metrics")
def requests():
    res = []
    for k,v in graphs.items():
        res.append(prometheus_client.generate_latest(v))
    return Response(res, mimetype="text/plain")

