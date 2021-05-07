# Backend

## Project setup
Install development dependencies
```
pipenv install --dev
```

Create a `.env` file containing dev settings
```toml
GITHUB_USERNAME=<github-username>
GITHUB_TOKEN=<personal-access-token>
```

### Compiles and hot-reloads for development
```
pipenv run serve
```

### Lints and fixes files
```
pipenv run lint
```

## Docker image

### Build image
```
docker build -t portfolio-backend .
```

### Run image
```pylint
docker run -p 8000:80 -e GITHUB_USERNAME -e GITHUB_TOKEN portfolio-backend
```

with
- **GITHUB_USERNAME**: name of the user repos will be fetched when looking for projects.
- **GITHUB_TOKEN**: personal access token that allow read only access to github API for given user.
