## Запуск приложения
```
helm install nginx-ingress-controller nginx-stable/nginx-ingress --set controller.service.httpPort.port=80 --set controller.enableSnippets=True
kubectl apply -f secrets.yaml
kubectl apply -f django-config.yaml
kubectl apply -f postgres-pv.yaml
kubectl apply -f postgres-pvc.yaml
kubectl apply -f postgres-deployment.yaml
kubectl apply -f postgres-svc.yaml
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f ingress.yaml
```
