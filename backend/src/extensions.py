from src.settings import GITHUB_USERNAME, GITHUB_TOKEN
from .github import Github

github = Github(GITHUB_USERNAME, GITHUB_TOKEN)
