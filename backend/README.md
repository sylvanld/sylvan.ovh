
## Deployment

Create a kubernetes secret containing sensitive information required by backend.

```bash
kubectl create secret generic portfolio-secret --from-literal='GITHUB_USERNAME=<something>' --from-literal='GITHUB_TOKEN=<something>'
```

Then you can deploy portfolio services using `deployment.yml` manifest.
