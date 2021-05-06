from pydantic import BaseModel
from datetime import datetime
from dataclasses import dataclass


class APIModel(BaseModel):
    class Config:
        orm_mode = True


class Repository(APIModel):
    id: int
    name: str
    full_name: str
    description: str = None

    license: str = None
    forked: bool
    private: bool

    open_issues_count: int
    commits_count: int
    stargazers_count: int
    watchers_count: int

    repository_url: str
    showcase_url: str = None

    created_at: datetime
    updated_at: datetime
