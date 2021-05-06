import requests
from urllib.parse import urljoin
from datetime import datetime

from src.models import Repository


def parse_datetime(datestring: str) -> datetime:
    datestring = datestring.replace("Z", "+00:00")
    return datetime.fromisoformat(datestring)


def load_repository(data: dict) -> Repository:
    return Repository(
        id=data["id"],
        name=data["name"],
        full_name=data["full_name"],
        description=data["description"],
        license=data["license"].get("name") if data["license"] else None,
        private=data["private"],
        forked=data["fork"],
        open_issues_count=data["open_issues_count"],
        commits_count=data["size"],
        stargazers_count=data["stargazers_count"],
        watchers_count=data["watchers_count"],
        repository_url=data["html_url"],
        created_at=parse_datetime(data["created_at"]),
        updated_at=parse_datetime(data["updated_at"]),
        showcase_url=data["homepage"] or None,
    )


class Github(requests.Session):
    def __init__(self, username, access_token):
        super(Github, self).__init__()
        self.base_url = "https://api.github.com"
        self.username = username
        self.auth = (username, access_token)
        self.headers = {"Accept": "application/vnd.github.v3+json"}

    def request(self, method, url, *args, **kwargs):
        url = urljoin(self.base_url, url)
        return super(Github, self).request(method, url, *args, **kwargs)

    def get_my_repositories(self):
        response = self.get(f"/users/{self.username}/repos")
        import json

        with open("toto.json", "w") as toto:
            json.dump(response.json(), toto, indent=4)
        return [load_repository(repo_data) for repo_data in response.json()]


if __name__ == "__main__":
    from settings import GITHUB_USERNAME, GITHUB_TOKEN

    github = Github(GITHUB_USERNAME, GITHUB_TOKEN)
    repositories = github.get_my_repositories()

    for repository in repositories:
        print(repository)
