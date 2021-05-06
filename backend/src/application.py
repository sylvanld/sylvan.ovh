from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from typing import List
from src.models import Repository
from src.extensions import github

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
