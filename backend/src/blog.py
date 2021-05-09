import os
import json
import logging
import subprocess

from typing import List
from datetime import datetime
from pydantic import BaseModel
from src.models import IndexArticle, IndexData


LOGGER = logging.getLogger(__name__)

BLOG_DIRECTORY = '/tmp/blog'


class BlogIndex:
    def __init__(self):
        self.init_index()

    def init_index(self):
        try:
            with open(os.path.join(BLOG_DIRECTORY, 'index.json')) as blog_index_file:
                self.__index = IndexData.parse_obj(json.load(blog_index_file))
        except FileNotFoundError:
            self.__index = IndexData(articles=[])
            self.__save()
            
    def __save(self):
        with open(os.path.join(BLOG_DIRECTORY, 'index.json'), 'w') as blog_index_file:
            blog_index_file.write(self.__index.json(indent=4))
        subprocess.call(['git', 'add', 'index.json'], cwd=BLOG_DIRECTORY)

    def get_articles(self):
        return self.__index.articles

    def create_article(self, article_name):
        self.__index.articles.append(
            IndexArticle(
                article_name=article_name,
                created_at=datetime.now(), 
                updated_at=datetime.now())
        )
        self.__save()

    def update_article(self, old_name, new_name):
        entry = next(entry for entry in self.__index.articles if entry.article_name == old_name)
        entry.article_name = new_name
        entry.updated_at = datetime.now()
        self.__save()

    def delete_article(self, article_name):
        index = next(k for k in range(len(self.__index.articles)) if self.__index.articles[k].article_name == article_name)
        self.__index.articles.pop(index)
        self.__save()



class BlogRepository:
    def __init__(self, repository_url, username, token):
        self.init_repository(repository_url, username, token)

    def authenticated_url(self, repository_url, username, token):
        """
        Take url like http://example.com and convert it to http://user:pass@example.com
        """
        parts = repository_url.split('/')
        parts[2] = f'{username}:{token}@{parts[2]}'
        return '/'.join(parts)

    def init_repository(self, repository_url, username, token):
        """
        Ensure blog repository is correctly initialized locally.
        """
        try:
            os.makedirs('/tmp/blog')
            subprocess.call(['git', 'init'], cwd=BLOG_DIRECTORY)
            subprocess.call(['git', 'remote', 'add', 'origin', self.authenticated_url(repository_url, username, token)], cwd=BLOG_DIRECTORY)
            subprocess.call(['git', 'checkout', '--orphan', 'blog'], cwd=BLOG_DIRECTORY)
            subprocess.call(['git', 'pull', 'origin', 'blog'], cwd=BLOG_DIRECTORY)
        except FileExistsError:
            LOGGER.info("File exists")

    def create_article(self, article_name, content):
        # write new file content to the disk
        with open(os.path.join(BLOG_DIRECTORY, article_name), 'w') as file:
            file.write(content)
        # commit changes and push
        subprocess.call(['git', 'add', article_name], cwd=BLOG_DIRECTORY)

    def update_article(self, old_name, new_name, content):
        # do renaming if name changed
        if old_name != new_name:
            self.rename_article(old_name, new_name)
        # write new file content to the disk
        with open(os.path.join(BLOG_DIRECTORY, new_name), 'w') as file:
            file.write(content)
        # commit changes and push
        subprocess.call(['git', 'add', new_name], cwd=BLOG_DIRECTORY)

    def rename_article(self, old_name, new_name):
        # move file under a new name
        subprocess.call(['mv', old_name, new_name], cwd=BLOG_DIRECTORY)
        # commit changes and push
        subprocess.call(['git', 'add', old_name, new_name], cwd=BLOG_DIRECTORY)
        subprocess.call(['git', 'commit', '-m', 'Rename article %s -> %s' % (old_name, new_name)], cwd=BLOG_DIRECTORY)

    def delete_article(self, article_name):
        # remove article file
        subprocess.call(['rm', article_name], cwd=BLOG_DIRECTORY)
        # commit changes and push
        subprocess.call(['git', 'add', article_name], cwd=BLOG_DIRECTORY)


class Blog:
    def __init__(self, repository, username, token):
        self.repository = BlogRepository(repository, username, token)
        self.index = BlogIndex()

    def save(self, commit_message):
        subprocess.call(['git', 'commit', '-m', commit_message], cwd=BLOG_DIRECTORY)
        subprocess.call(['git', 'push', '-u', 'origin', 'blog'], cwd=BLOG_DIRECTORY)

    def get_articles(self):
        return self.index.get_articles()

    def create_article(self, article_name, content):
        self.index.create_article(article_name)
        self.repository.create_article(article_name, content)
        self.save('Create article %s' % article_name)
    
    def update_article(self, old_name, new_name, content):
        self.index.update_article(old_name, new_name)
        self.repository.update_article(old_name, new_name, content)
        self.save('Edit article %s' % old_name)

    def delete_article(self, article_name):
        self.index.delete_article(article_name)
        self.repository.delete_article(article_name)
        self.save('Delete article %s' % article_name)
