# Exposing publicly applications on AWS EKS with Traefik Ingress Controller

Demo of exposing public applications on AWS EKS with Traefik Proxy. This repository is a part of [Dev.to article]()

### Prerequisites

- preconfigure EKS Cluster with [AWS Load Balancer Controller](https://github.com/kubernetes-sigs/aws-load-balancer-controller) and [External DNS](https://github.com/kubernetes-sigs/external-dns) installed - you can leverages my repo that will help you setup EKS cluster with `eksctl` - [GitHub repo](https://github.com/luafanti/eksctl-labs-cluster)
- Route53 domain with ACM Certificate

### Installation TL;DR

!!! Before install replace all occurrences of `<YOUR_CERTIFICATE_ARN>` and `<YOUR_DOMAIN>` in all repo resources.

Install Traefik
```bash
helm repo add traefik https://helm.traefik.io/traefik
helm install traefik traefik/traefik --create-namespace --namespace=network --values=helm/traefik.yaml 
```

Install samples apps (RabbitMQ and PostgreSQL):
```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm install rabbitmq bitnami/rabbitmq --create-namespace --namespace=messaging -f helm/rabbitmq.yaml
helm install postgres bitnami/postgresql --create-namespace --namespace=database -f helm/postgres.yaml
```

Apply Traefik route resources:
```bash
kubectl apply -f network/traefik-dashboard-route.yaml
kubectl apply -f network/postgres-route.yaml
kubectl apply -f network/rabbitmq-route.yaml
```

### Testing utils

```bash
psql -h postgres.<YOUR_DOMAIN> -p 5432 -U root
# pass 'root' password

python3 utils/rabbitmq_ampq_test.py

#In browser:
https://rabbitmq.<YOUR_DOMAIN>
https://traefik.<YOUR_DOMAIN>:9000/dashboard/
```

### Cleanup

```bash
helm uninstall rabbitmq -n messaging
helm uninstall postgres -n database
helm uninstall traefik -n network

# Delete cluster create with eksctl-labs-cluster repo
eksctl delete cluster -f cluster.yaml --disable-nodegroup-eviction
```
