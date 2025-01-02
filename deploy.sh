docker build -f api/Dockerfile -t document-processor:latest .
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
pytest tests/