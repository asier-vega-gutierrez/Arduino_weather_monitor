from flask import Response, Flask, request
import prometheus_client
from prometheus_client.core import CollectorRegistry
from prometheus_client import Summary, Counter, Histogram, Gauge
import time
import random




app = Flask(__name__)

#Metrics to measure
graphs = {}
graphs['temp'] = Gauge('temperature_in_celsius_1', 'Temperature in Celsius')
graphs['press'] = Gauge('atmospheric_pressure_1', 'Atmostpheric Pressure')
graphs['hum'] = Gauge('humidity_1', 'Percentage of Humidity')
graphs['w_speed'] = Gauge('wind_speed_1', 'The speed of the wind in m/s')
graphs['w_dir'] = Gauge('wind_direction_1', 'The direction of the wind in degrees')
graphs['rain'] = Gauge('rain_precipitation_1', 'Rain precipitations in l/m^2')


#Inicialization of applicaton where we set the metrics
@app.route("/", methods=['GET'])
def hello():
    return "Hello World!" 

#Get Metrics
@app.route("/metrics")
def requests():
    while True:
        graphs['temp'].set(random.randrange(10))
        graphs['press'].set(random.randrange(10))
        graphs['hum'].set(random.randrange(10))
        graphs['w_speed'].set(random.randrange(10))
        graphs['w_dir'].set(random.randrange(10))
        graphs['rain'].set(random.randrange(10))
        res = []
        for k,v in graphs.items():
            res.append(prometheus_client.generate_latest(v))
        return Response(res, mimetype="text/plain")

