from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from typing import List
from src.models import Repository, IndexArticle, FullArticle, EditArticle
from src.extensions import github, blog

api = FastAPI(
    title="Showcase site API",
    info={"contact": {"name": "Sylvan Le Deunff", "email": "sledeunf@gmail.com"}},
)
api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@api.get("/github/my/repositories", response_model=List[Repository])
def get_my_repositories():
    return github.get_my_repositories()

@api.get("/blog/articles/{code}", response_model=FullArticle)
def get_blog_article(code: str):
    return blog.get_article(code)

@api.get("/blog/articles", response_model=List[IndexArticle])
def get_blog_article():
    return blog.get_articles()

@api.post("/blog/articles")
def create_blog_article(article: EditArticle):
    blog.create_article(article.code, article.title, article.content)

@api.put("/blog/articles/{code}")
def update_blog_article(code: str, article: EditArticle):
    return blog.update_article(code, article.code, article.title, article.content)

@api.delete("/blog/articles/{code}")
def delete_blog_post(code: str):
    blog.delete_article(code)
