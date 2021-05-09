from src.settings import GITHUB_USERNAME, GITHUB_TOKEN, BLOG_REPOSITORY
from src.github import Github
from src.blog import Blog

github = Github(GITHUB_USERNAME, GITHUB_TOKEN)
blog = Blog(BLOG_REPOSITORY, username=GITHUB_USERNAME, token=GITHUB_TOKEN)
