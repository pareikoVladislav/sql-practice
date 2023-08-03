from helpers import get_datetime_string
import json
from db_conn import Database
from models import Post


class PostsManager:
    def __init__(self):
        self.db_conn = Database()

    def get_post_id_by_title(self, post_title: str):
        post = self.db_conn.session.query(Post).filter_by(
            title=post_title
        ).first()

        return post.id

    def get_post_by_id(self, post_id: int):
        post = self.db_conn.session.query(Post).filter_by(
            id=post_id
        ).first()

        post_info: dict = {
            "id": post.id,
            "title": post.title,
            "content": post.content,
            "created_at": post.created_at,
            "updated_at": post.updated_at,
            "author": {
                "id": post.author.id,
                "username": post.author.username,
            },
            "comments": [],
        }

        for comment in post.comments:
            comment_info: dict = {
                "id": comment.id,
                "content": comment.content,
                "author_id": comment.author.id,
                "created_at": comment.created_at,
                "updated_at": comment.updated_at,
            }
            post_info['comments'].append(comment_info)

        return json.dumps(post_info, indent=4)

    def update_post_title(self, post_id: int):
        post = self.db_conn.session.query(Post).filter_by(
            id=post_id).first()

        post.title = input("Enter new title: ")
        post.updated_at = get_datetime_string()

        self.db_conn.commit_changes()

    def delete_post(self, post_id: int):
        post = self.db_conn.session.query(Post).filter_by(
            id=post_id).first()

        self.db_conn.session.delete(post)
        self.db_conn.commit_changes()
