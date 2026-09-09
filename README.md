# 🚀 Django GitOps Platform on Kubernetes

Automated deployment of a Django/Gunicorn application on Minikube using ArgoCD (GitOps).

---

## 🛠️ Architecture

* **App:** Django 5.x / Gunicorn WSGI
* **Container:** Docker (`python:3.12-slim`)
* **Orchestration:** Kubernetes (Minikube)
* **GitOps:** ArgoCD (Auto-sync from `k8s/`)

---

## 📁 Repository Structure

```text
.
├── Dockerfile          # Multi-stage image build
├── argocd-app.yaml     # ArgoCD Application manifest
├── k8s/                # K8s Deployment & Service manifests
├── mysite/             # Django config (includes /healthz route)
└── requirements.txt    # Python dependencies
```

# ⚡ Quickstart
Set Minikube Docker environment:

---
eval $(minikube docker-env)
Build the container image:

---
docker build -t django-mysite:v1 .

## Deploy via ArgoCD:

kubectl apply -f argocd-app.yaml

Verify deployment status:

kubectl get application django-k8s-platform -n argocd
# 🧪 Healthcheck & Diagnostics
Port-Forward to local machine:

kubectl port-forward svc/argocd-server -n argocd 8081:443
kubectl -n argocd get secret argocd-initial-admin-secret \
  -o jsonpath="{.data.password}" | base64 -d && echo
kubectl port-forward svc/django-service 8080:80
Test the /healthz endpoint:

curl -i http://localhost:8080/healthz
View application logs:

kubectl logs -l app=django-app --tail=50

# Local Development

## Local

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python manage.py runserver

## Docker

docker build -t django-mysite:v1 .
docker run ...

## Kubernetes

minikube start
kubectl get nodes

## Argo CD

kubectl apply -f argocd-app.yaml
kubectl get application -n argocd
