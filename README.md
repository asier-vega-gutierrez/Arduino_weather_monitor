Pasos para montar todo:

    Kubernetes:

    0. Iniciar minikube "minikube start"
    
    1. Abrir terminal en "src/arquitectura/kubernetes/."
    
    2. Ejecutar "eval $(minikube docker-env)"
    
    3. Ejecutar "docker build -t flask-app python/"
    
    4. Ejecutar "kubectl create namespace monitoring"
    
    5. Ejecutar "kubectl apply -f grafana/ -n monitoring"
    
    6. Ejecutar "kubectl apply -f prometheus/ -n monitoring"
    
    7. Ejecutar "kubectl apply -f python/ -n monitoring"
    
    8. En otra terminal ejecutart "minikube tunnel"

