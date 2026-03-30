# DevOps Platform

Portfolio de proyectos DevOps construidos desde cero, simulando entornos reales de producción.  
**Juan Diego Monje** — Junior DevOps Engineer en transición desde IT Support.

[🌐 Portfolio](https://monjju.github.io) · [🔗 LinkedIn](https://linkedin.com/in/juan-monje-pulecio) · [📦 GitHub](https://github.com/monjju)

---

## 🏗️ Proyectos

### ☸️ Proyecto 1 — Kubernetes Platform
Plataforma cloud-native con app Python/Flask, 3 réplicas, HPA autoscaling, Ingress y observabilidad completa con Prometheus, Grafana y Loki.  
**Stack:** Kubernetes · Docker · Helm · Prometheus · Grafana · Loki  
[→ Ver proyecto](./proyecto-1-kubernetes)

### 🛡️ Proyecto 2 — CI/CD Pipeline DevSecOps
Pipeline de 4 stages con GitHub Actions: validate, build Docker multi-stage, security scan con Trivy y Gitleaks, y firma de imagen con Cosign. Todo en verde.  
**Stack:** GitHub Actions · Docker · Trivy · Gitleaks · Cosign  
[→ Ver proyecto](./proyecto-2-cicd)

### ☁️ Proyecto 3 — Terraform + AWS Infrastructure as Code
Infraestructura AWS con Terraform modular: VPC multi-AZ, EKS cluster, RDS PostgreSQL, IAM roles y remote state en S3 con DynamoDB locking. Desarrollado y validado con LocalStack.  
**Stack:** Terraform · AWS · LocalStack · EKS · VPC · RDS  
[→ Ver proyecto](./proyecto-3-terraform)

### 🔄 Proyecto 4 — GitOps con ArgoCD
El proyecto que conecta todo lo anterior. Cada push a GitHub desencadena el pipeline completo — build, scan, firma — y ArgoCD despliega automáticamente al cluster sin tocar kubectl. El rollback es un `git revert`.  
**Stack:** ArgoCD · Kustomize · Helm · GitHub Actions · k3d  
[→ Ver proyecto](./proyecto-4-gitops)

---

## 🛠️ Stack general

![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat&logo=kubernetes&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=flat&logo=terraform&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=github-actions&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat&logo=amazon-aws&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=flat&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=flat&logo=grafana&logoColor=white)
![ArgoCD](https://img.shields.io/badge/ArgoCD-EF7B4D?style=flat&logo=argo&logoColor=white)

---

## 📖 Lo que he aprendido construyendo esto

Vengo de IT Support. Antes de estos proyectos no había tocado Kubernetes, Terraform ni GitOps. Todo lo que ves aquí lo construí resolviendo problemas reales — algunos fáciles, muchos no.

- **IaC no es opcional** — infraestructura declarativa, versionada y reproducible. Sin cambios manuales no trazables
- **El .gitignore va primero** — aprendido después de intentar subir un binario de 648MB a GitHub
- **Seguridad por diseño** — redes privadas, IAM con mínimo privilegio, scan en el pipeline. No se añade al final
- **GitOps cambia la forma de pensar** — el cluster es un reflejo de Git, no al revés
- **Los errores enseñan más** — conflictos de Git, puertos bloqueados, providers incompatibles, ImagePullBackOff. Cada fallo tiene una lección

Soy junior y lo sé. Pero cada proyecto aquí representa un problema real resuelto, una decisión técnica justificada y algo que entiendo de verdad.

### 📊 Proyecto 5 — Observabilidad Avanzada con OpenTelemetry
Stack completo de observabilidad con los 3 pilares: métricas (Prometheus), logs (Loki) y trazas distribuidas (Tempo). App Flask instrumentada con OpenTelemetry SDK. Correlación entre señales por trace_id.  
**Stack:** OpenTelemetry · Prometheus · Grafana · Loki · Tempo · Kubernetes  
[→ Ver proyecto](./proyecto-5-observabilidad)
