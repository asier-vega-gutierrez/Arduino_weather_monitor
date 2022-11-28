# Prometheus Application Monitoring

To run any of the commands, please ensure you open a terminal and navigate to the path where this readme is located.

## Start Prometheus, Grafana & Dashboards

```
docker-compose up -d prometheus
docker-compose up -d grafana
docker-compose up -d grafana-dashboards
docker-compose up -d --build python-application
```