Pasos para montar todo:

    
    Ejecutar servidro web y aplicacion de percepcion en arduino: 

    0. Connectar arduino a ordenador

    1. Cargar y ejecutar codigo de reset (EstacionMeteorologica/src/wifi/HardwareFactoryReset/)

    2. Cargar y ejecutar codigo de inicio (EstacionMeteorologica/src/wifi/SpiUartTerminal/)

    3. Abrir monitor serie y con el modo de "no line ending" ejecutar lo siguientes comandos:

    4. "$$$"

    5. Cambiar el modo del monitor serie a "carriage return" y ejecutar lo siguientes comandos:

    6. "scan" "set wlan auth <value>" "set wlan phrase <passphrase>" "join <ssid>" "set wlan ssid <ssid>" "set wlan join 1" "save"

    7. Cargar y ejecutar codigo de inicio del servidor "EstacionMeteorologica/src/wifi/PruebaSrvr/"

    8. Acceda via navegar a la ip que este codigo devulva desde el monitor serie

    
    Montar arquitectura CNF en minikube:

    0. Iniciar minikube "minikube start"
    
    1. Abrir terminal en "src/arquitectura/kubernetes/."
    
    2. Ejecutar "eval $(minikube docker-env)"
    
    3. Ejecutar "docker build -t flask-app python/"
    
    4. Ejecutar "kubectl create namespace monitoring"
    
    5. Ejecutar "kubectl apply -f grafana/ -n monitoring"
    
    6. Ejecutar "kubectl apply -f prometheus/ -n monitoring"
    
    7. Ejecutar "kubectl apply -f python/ -n monitoring"
    
    8. En otra terminal ejecutart "minikube tunnel"

