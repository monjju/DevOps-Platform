# Proyecto 1 — Kubernetes Platform

Plataforma cloud-native completa desplegada en Kubernetes local con k3d.  
Forma parte del portfolio DevOps de [Juan Diego Monje](https://monjju.github.io).

## ¿Qué incluye?

App Python/Flask con 3 réplicas, load balancing, HPA autoscaling, Ingress y stack de observabilidad completo.

## Arquitectura
```
k3d Cluster (local)
├── app/                    → Python/Flask (3 réplicas)
│   ├── Deployment          → 3 réplicas con rolling update
│   ├── Service             → Load balancing interno
│   ├── HPA                 → Autoscaling (1-5 réplicas)
│   └── Ingress             → Enrutamiento HTTP
└── observabilidad/
    ├── Prometheus          → Métricas
    ├── Grafana             → Dashboards
    └── Loki                → Logs
```

## Stack

| Herramienta | Uso |
|-------------|-----|
| Kubernetes (k3d) | Orquestación de contenedores |
| Docker | Containerización |
| Helm | Gestión de paquetes K8s |
| Prometheus | Recolección de métricas |
| Grafana | Visualización |
| Loki | Agregación de logs |

## Decisiones técnicas

- ✅ HPA configurado — escala automáticamente según CPU
- ✅ Rolling updates — zero downtime deployments
- ✅ Ingress — punto de entrada único para el tráfico
- ✅ Observabilidad completa — métricas, dashboards y logs centralizados

## Cómo ejecutarlo
```bash
# Crear cluster
k3d cluster create devops-platform

# Desplegar app
kubectl apply -f Kubernetes/base/

# Instalar observabilidad
helm install prometheus prometheus-community/kube-prometheus-stack
helm install loki grafana/loki-stack
```

## Autor

**Juan Diego Monje** — Junior DevOps Engineer  
[GitHub](https://github.com/monjju) · [LinkedIn](https://linkedin.com/in/juan-monje-pulecio) · [Portfolio](https://monjju.github.io)
