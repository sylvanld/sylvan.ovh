# Portfolio

*Portfolio application to showcase Github projects and introduce myself to the curious people*

## Structure

This project is a 2-tiers application composed of a [frontend](frontend/) and a [backend](backend/).

## Deployment using Kubernetes

### Create a Secret with sensitive environment variables

Create a kubernetes secret containing sensitive information required by backend.

```bash
kubectl create secret generic portfolio-secret --from-literal='GITHUB_USERNAME=<something>' --from-literal='GITHUB_TOKEN=<something>'
```

Then you can deploy portfolio services using `deployment.yml` manifest.

### Deploy frontend & backend using manifest

```bash
kubectl apply -f deployment.yml [-n <your-namespace>]
```