from flask import Response, Flask, request
import prometheus_client
from prometheus_client.core import CollectorRegistry
from prometheus_client import Summary, Counter, Histogram, Gauge
import time
import random




app = Flask(__name__)
indice = [1,2]
graphs = {}
#Metrics to measure
for n in indice:
    graphs['temp_'+str(n)] = Gauge('temperature_in_celsius_'+str(n), 'Temperature in Celsius')
    graphs['press_'+str(n)] = Gauge('atmospheric_pressure_'+str(n), 'Atmostpheric Pressure')
    graphs['hum_'+str(n)] = Gauge('humidity_'+str(n), 'Percentage of Humidity')
    graphs['w_speed_'+str(n)] = Gauge('wind_speed_'+str(n), 'The speed of the wind in m/s')
    graphs['w_dir_'+str(n)] = Gauge('wind_direction_'+str(n), 'The direction of the wind in degrees')
    graphs['rain_'+str(n)] = Gauge('rain_precipitation_'+str(n), 'Rain precipitations in l/m^2')
    graphs['light_'+str(n)] = Gauge('light_level_'+str(n), 'Light level')


#Inicialization of applicaton where we set the metrics
@app.route("/", methods=['GET'])
def hello():
    return "Hello World!" 

#Get Metrics
@app.route("/metrics")
def requests():
    while True:
        graphs['temp_1'].set(random.randint(-5, 50))
        graphs['press_1'].set(random.randint(885, 1077))
        graphs['hum_1'].set(random.randint(0,100))
        graphs['w_speed_1'].set(random.randint(0, 40))
        graphs['w_dir_1'].set(random.randint(0,360))
        graphs['rain_1'].set(random.randint(0, 3))
        graphs['light_1'].set(random.randint(0,100))
        res = []
        for k,v in graphs.items():
            res.append(prometheus_client.generate_latest(v))
        return Response(res, mimetype="text/plain")

