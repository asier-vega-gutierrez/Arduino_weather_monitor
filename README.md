## Desarrollo de aplicación IoT para monitorización de estaciones meteorológicas
<ul>
    <li>Fechas: Septiembre 2022 - Diciembre 2022</li>
    <li>Descripción: Las estaciónes están montadas con un sistema embebido Arduino que centraliza los sensores de una estación. Se emplea un módulo Wifi para transmitir los datos a la arquitectura CNF, montada con Kubernetes en el cluster Minikube. Esta arquitectura está compuesta de un pod de Prometheus que almacena los datos y de un pod de Grafana para visualizarlos. Además se implementa un sistema de alarmas utilizando el servidor SMTP de Google Mail.</li>
    <li>Herramientas utilizadas:</li>
<a href="https://grafana.com/" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/grafana/grafana-original.svg" alt="grafana" width="40" height="40"/> 
</a>
<a href="https://prometheus.io/" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/prometheus/prometheus-original.svg" alt="prometheus" width="40" height="40"/> 
</a>
<a href="https://kubernetes.io/" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/kubernetes/kubernetes-plain.svg" alt="kubernetes" width="40" height="40"/> 
</a>
<a href="https://www.arduino.cc/" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/arduino/arduino-original.svg" alt="arduino" width="40" height="40"/> 
</a>
</ul>

### Pasos para montar todo:

    **Ejecutar servidor web y aplicacion de percepcion en Arduino:** 
    0. Connectar arduino a ordenador
    1. Cargar y ejecutar codigo de reset (EstacionMeteorologica/src/wifi/HardwareFactoryReset/)
    2. Cargar y ejecutar codigo de inicio (EstacionMeteorologica/src/wifi/SpiUartTerminal/)
    3. Abrir monitor serie y con el modo de "no line ending" ejecutar lo siguientes comandos:
    4. "$$$"
    5. Cambiar el modo del monitor serie a "carriage return" y ejecutar lo siguientes comandos:
    6. "scan" "set wlan auth <value>" "set wlan phrase <passphrase>" "join <ssid>" "set wlan ssid <ssid>" "set wlan join 1" "save"
    7. Cargar y ejecutar codigo de inicio del servidor "EstacionMeteorologica/src/wifi/PruebaSrvr/"
    8. Acceda via navegar a la ip que este codigo devulva desde el monitor serie

    **Montar arquitectura CNF en Minikube:**
    0. Iniciar minikube "minikube start"
    1. Abrir terminal en "src/arquitectura/kubernetes/."
    2. Ejecutar "eval $(minikube docker-env)"
    3. Ejecutar "docker build -t flask-app python/"
    4. Ejecutar "kubectl create namespace monitoring"
    5. Ejecutar "kubectl apply -f grafana/ -n monitoring"
    6. Ejecutar "kubectl apply -f prometheus/ -n monitoring"
    7. Ejecutar "kubectl apply -f python/ -n monitoring"
    8. En otra terminal ejecutar "minikube tunnel"

