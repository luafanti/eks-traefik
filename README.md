# Exposing publicly applications on AWS EKS with Traefik Ingress Controller

Demo of exposing publicly applications on AWS EKS with Traefik Ingress Controller. This repository is a part of [Dev.to article]()

### Prerequisites

- preconfigure EKS Cluster with [AWS Load Balancer Controller](https://github.com/kubernetes-sigs/aws-load-balancer-controller) and [External DNS](https://github.com/kubernetes-sigs/external-dns) installed - you can leverages my repo that will help you setup EKS cluster with `eksctl` - [GitHub repo](https://github.com/luafanti/eksctl-labs-cluster)
- Route53 domain with ACM Certificate

### Installation TL;DR

As always I encourage you to install kubectx+kubens to navigate Kubernetes easily.
```bash
helm repo add traefik https://helm.traefik.io/traefik
helm install traefik traefik/traefik --create-namespace --namespace=network --values=helm/traefik.yaml 
```
