# DevOps Platform

Production-grade Kubernetes platform with full observability stack.

## Architecture
```
App (Python/Flask)
  └── Kubernetes (k3d)
        ├── 3 replicas with HPA
        ├── Prometheus (metrics)
        ├── Grafana (dashboards)
        └── Loki (logs)
```

## Stack

- **Container orchestration:** Kubernetes (k3d)
- **Application:** Python/Flask
- **Monitoring:** Prometheus + Grafana
- **Logging:** Loki + Promtail
- **Package manager:** Helm

## Quick Start

### Prerequisites
- Docker Desktop
- kubectl
- k3d
- Helm

### Deploy
```bash
# Create cluster
k3d cluster create devops-platform \
  --agents 2 \
  --port "80:80@loadbalancer" \
  --port "443:443@loadbalancer"

# Build and import image
docker build -t devops-platform:v1.0 ./app
k3d image import devops-platform:v1.0 -c devops-platform

# Deploy app
kubectl apply -f kubernetes/base/

# Deploy monitoring stack
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update

helm install prometheus-stack prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --create-namespace \
  --version 45.7.1 \
  --set grafana.adminPassword=devops123

helm install loki grafana/loki-stack \
  --namespace monitoring \
  --version 2.9.11 \
  --set grafana.enabled=false \
  --set prometheus.enabled=false
```

### Access
```bash
# App
kubectl port-forward svc/devops-platform 8080:80

# Grafana (admin/devops123)
kubectl port-forward svc/prometheus-stack-grafana 3000:80 -n monitoring
```

## Endpoints

| Endpoint | Description |
|----------|-------------|
| `/health` | Health check (used by K8s probes) |
| `/api/info` | Server info + hostname (shows load balancing) |
| `/api/stress` | CPU stress test (generates metrics) |

## What I learned

- Kubernetes core concepts: Deployments, Services, Probes, Resource limits
- Helm for package management
- Prometheus + Grafana for metrics visualization
- Loki + Promtail for centralized log aggregation
- Docker multi-stage builds
- Kubernetes load balancing in action
