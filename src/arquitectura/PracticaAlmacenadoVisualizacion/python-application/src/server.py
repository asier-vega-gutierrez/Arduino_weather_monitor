from flask import Response, Flask, request
import prometheus_client
from prometheus_client.core import CollectorRegistry
from prometheus_client import Summary, Counter, Histogram, Gauge


app = Flask(__name__)

graphs = {}
graphs['valor'] = Gauge('valor_criptomonedas', 'valor_criptomonedas')

#hace un get a esa url y del json de vuelta recuepero el valor "ultimo precio"
def valor():
    req = request.get_json('https://api.bitfinex.com/v1/pubticker/btcusd')
    return(req['last_price'])

@app.route("/")
def hello():
    return "Hello World!" 

@app.route("/metrics", methods=['GET'])
def requests():
    while True:
        graphs['valor'].set(valor())
        res = []
        for k,v in graphs.items():
            res.append(prometheus_client.generate_latest(v))
        return Response(res, mimetype="text/plain")

