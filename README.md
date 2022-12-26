##Pasos para montar todo:

#Kubernetes:
    0. Abrir terminal en "src/arquitectura/kubernetes/."
    
    1. Ejecutar "eval $(minikube docker-env)"
    
    2. Ejecutar "docker build -t flask-app python/"
    
    3. Ejecutar "kubectl create namespace monitoring"
    
    4. Ejecutar "kubectl apply -f grafana/ -n monitoring"
    
    5. Ejecutar "kubectl apply -f prometheus/ -n monitoring"
    
    6. Ejecutar "kubectl apply -f alermanager/ -n monitoring"
    
    7. Ejecutar "kubectl apply -f python/ -n monitoring"
    
    8. En otra terminal ejecutart "minikube tunnel"

