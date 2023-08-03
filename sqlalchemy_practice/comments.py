from sqlalchemy.exc import NoResultFound

from helpers import get_datetime_string
import json
from db_conn import Database
from models import Comment


class CommentsManager:
    def __init__(self):
        self.db_conn = Database()

    def get_all_comments(self):
        comments = self.db_conn.session.query(Comment).all()

        comments_info = []

        for comment in comments:
            comment_info = {
                "id": comment.id,
                "content": comment.content,
                "created_at": comment.created_at,
                "updated_at": comment.updated_at,
                "author_info": {
                    "id": comment.author.id,
                    "username": comment.author.username,
                },
            }
            comments_info.append(comment_info)

        return json.dumps(comments_info, indent=4)

    def get_comment_by_id(self, comment_id: int):
        comment = self.db_conn.session.query(Comment).filter_by(
            id=comment_id
        ).first()

        comment_info = {
            "id": comment.id,
            "content": comment.content,
            "created_at": comment.created_at,
            "updated_at": comment.updated_at,
            "author_info": {
                "id": comment.author.id,
                "username": comment.author.username,
            },
            "post_info": {
                "id": comment.post.id,
                "author_id": comment.author.id,
                "author_name": comment.author.username,
                "title": comment.post.title,
                "content": comment.post.content,
                "created_at": comment.post.created_at,
                "updated_at": comment.post.updated_at,
            }
        }

        return json.dumps(comment_info, indent=4)

    def update_comment(self, comment_id: int):
        comment = self.db_conn.session.query(Comment).filter_by(
            id=comment_id
        ).first()

        if comment:
            comment.content = input("Enter new comment: ")
            comment.updated_at = get_datetime_string()

            self.db_conn.commit_changes()
        else:
            raise NoResultFound("Can't find comment with this ID.")

    def delete_comment(self, comment_id: int):
        comment = self.db_conn.session.query(Comment).filter_by(
            id=comment_id
        ).first()

        if comment:
            self.db_conn.session.delete(comment)
            self.db_conn.commit_changes()
        else:
            raise NoResultFound("Can't find comment with this ID.")
