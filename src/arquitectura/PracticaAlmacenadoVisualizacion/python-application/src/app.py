from prometheus_client import start_http_server, Gauge
import random
import time

VALOR = Gauge('valor_criptomonedas', 'valor_criptomonedas')

def valor():
    return(random.random())

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(5000)
    # Generate some requests.
    while True:
        time.sleep(1)
        VALOR.set(valor())