# DevOps Platform

Portfolio de proyectos DevOps construidos desde cero, simulando entornos reales de producción.  
**Juan Diego Monje** — Junior DevOps Engineer en transición desde IT Support.

[🌐 Portfolio](https://monjju.github.io) · [🔗 LinkedIn](https://linkedin.com/in/juan-monje-pulecio) · [📦 GitHub](https://github.com/monjju)

---

## 🏗️ Proyectos

### ☸️ Proyecto 1 — Kubernetes Platform
Plataforma cloud-native con app Python/Flask, 3 réplicas, HPA autoscaling, Ingress y observabilidad completa (Prometheus + Grafana + Loki).  
**Stack:** Kubernetes, Docker, Helm, Prometheus, Grafana, Loki  
[→ Ver proyecto](./proyecto-1-kubernetes)

### 🛡️ Proyecto 2 — CI/CD Pipeline DevSecOps
Pipeline de 4 stages con GitHub Actions: validate, build Docker multi-stage, security scan (Trivy + Gitleaks) y firma de imagen con Cosign. Todo en verde.  
**Stack:** GitHub Actions, Docker, Trivy, Gitleaks, Cosign  
[→ Ver proyecto](./proyecto-2-cicd)

### ☁️ Proyecto 3 — Terraform + AWS Infrastructure as Code
Infraestructura AWS con Terraform modular: VPC multi-AZ, EKS cluster, RDS PostgreSQL, IAM roles y remote state en S3 con DynamoDB locking. Desarrollado con LocalStack.  
**Stack:** Terraform, AWS, LocalStack, EKS, VPC, RDS  
[→ Ver proyecto](./proyecto-3-terraform)
🔄 Proyecto 4 — GitOps con ArgoCD

### 🔄 Proyecto 4 — GitOps con ArgoCD
Pipeline CI/CD conectado con ArgoCD — cada push a GitHub desencadena build, scan, firma y despliegue automático al cluster. Rollback con un simple `git revert`.  
**Stack:** ArgoCD, Kustomize, Helm, GitHub Actions, k3d  
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

---
## 📖 Lo que he aprendido construyendo este portfolio

Background en IT Support con transición práctica hacia entornos cloud-native. Este portfolio no está basado en tutoriales, sino en resolución de problemas reales y decisiones técnicas implementadas end-to-end.

- **IaC como estándar** — infraestructura declarativa, versionada y reproducible. Sin cambios manuales no trazables
- **Control desde el inicio** — correcta gestión del repositorio desde el primer commit: estructura, .gitignore, artefactos
- **Seguridad por diseño** — arquitecturas privadas (EKS, RDS), IAM con mínimo privilegio, sin exposición innecesaria
- **Optimización de coste** — uso de LocalStack para simular y validar infraestructura AWS sin impacto económico
- **Debugging como skill** — resolución de conflictos reales: providers, networking, Git, dependencias

Cada proyecto refleja decisiones técnicas justificadas, trade-offs evaluados y soluciones funcionales.
