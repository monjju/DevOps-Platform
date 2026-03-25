# Proyecto 2 — CI/CD Pipeline DevSecOps

Pipeline de seguridad completo con GitHub Actions integrado en el flujo de desarrollo.  
Forma parte del portfolio DevOps de [Juan Diego Monje](https://monjju.github.io).

## ¿Qué incluye?

4 stages automatizados que se ejecutan en cada push: validate, build, security scan y firma de imagen.

## Pipeline
```
Push → GitHub Actions
├── Stage 1: Validate    → lint, tests
├── Stage 2: Build       → Docker multi-stage image
├── Stage 3: Security    → Trivy (vulnerabilidades) + Gitleaks (secrets)
└── Stage 4: Sign        → Cosign (firma de imagen)
```

## Stack

| Herramienta | Uso |
|-------------|-----|
| GitHub Actions | Orquestación del pipeline |
| Docker | Build multi-stage |
| Trivy | Scan de vulnerabilidades |
| Gitleaks | Detección de secrets |
| Cosign | Firma de imágenes |

## Decisiones de seguridad

- ✅ Trivy — detecta CVEs en la imagen antes de desplegar
- ✅ Gitleaks — evita que secrets lleguen al repo
- ✅ Cosign — garantiza que la imagen no fue modificada post-build
- ✅ Multi-stage build — imagen final mínima, menor superficie de ataque

## Resultado

Todo en verde — pipeline completo sin errores ni vulnerabilidades críticas.

## Autor

**Juan Diego Monje** — Junior DevOps Engineer  
[GitHub](https://github.com/monjju) · [LinkedIn](https://linkedin.com/in/juan-monje-pulecio) · [Portfolio](https://monjju.github.io)
