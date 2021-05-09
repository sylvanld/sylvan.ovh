from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from typing import List
from src.models import Repository, IndexArticle, CreateArticle, UpdateArticle, DeleteArticle
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

@api.get("/blog/articles", response_model=List[IndexArticle])
def get_blog_article():
    return blog.get_articles()

@api.post("/blog/articles")
def create_blog_article(data: CreateArticle):
    blog.create_article(data.article_name, data.article_content)

@api.put("/blog/articles")
def update_blog_article(data: UpdateArticle):
    return blog.update_article(data.old_name, data.new_name, data.article_content)

@api.delete("/blog/articles")
def delete_blog_post(data: DeleteArticle):
    blog.delete_article(data.article_name)