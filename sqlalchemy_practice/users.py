import json
import bcrypt
import sqlalchemy.exc

from helpers import get_datetime_string
from db_conn import Database
from models import User, Post, Comment


class UserManager:
    def __init__(self):
        self.db_conn = Database()

    @staticmethod
    def hash_password(password: str):
        salt = bcrypt.gensalt()

        hashed_password = bcrypt.hashpw(
            password.encode('utf-8'), salt)

        return hashed_password

    def create_new_user(
            self, user_name: str, password: str,
            email: str, add_info: str) -> None:
        user = User(
            username=user_name,
            password=self.hash_password(password),
            email=email,
            additional_info=add_info,
            created_at=get_datetime_string()
        )
        self.db_conn.session.add(user)
        self.db_conn.commit_changes()

    def get_user_id_by_email(self, user_email: str) -> int:
        user = self.db_conn.session.query(User).filter_by(
            email=user_email
        ).first()

        return user.id

    def update_username_by_email(self, user_email: str) -> None:
        user = self.db_conn.session.query(User).filter_by(
            email=user_email
        ).first()

        user.username = input("Enter new user name: ")
        user.updated_at = get_datetime_string()
        self.db_conn.commit_changes()

    def get_all_users(self):
        all_users = self.db_conn.session.query(User).all()

        users_info: list = []

        for user in all_users:
            user_info: dict = {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "add_info": user.additional_info,
                "created_at": user.created_at,
                "posts": [],
                "comments": [],
            }
            for post in user.posts:
                post_info: dict = {
                    "id": post.id,
                    "author_id": post.author.id,
                    "post_author": post.author.username,
                    "post_title": post.title,
                }
                user_info['posts'].append(post_info)

            for comment in user.comments:
                comment_info: dict = {
                    "id": comment.id,
                    "comment_author": comment.author.username,
                    "comments_content": comment.content,
                    "created_at": comment.created_at,
                }
                user_info['comments'].append(comment_info)

            users_info.append(user_info)

        return json.dumps(users_info, indent=4)

    def get_user_by_id(self, user_id: int):
        user = self.db_conn.session.query(User).filter_by(
            id=user_id
        ).first()

        user_info: dict = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "add_info": user.additional_info,
            "created_at": user.created_at,
            "posts": [],
            "comments": [],
        }

        for post in user.posts:
            post_info: dict = {
                "id": post.id,
                "author_id": post.author.id,
                "post_author": post.author.username,
                "post_title": post.title,
            }
            user_info["posts"].append(post_info)

        for comment in user.comments:
            comment_info: dict = {
                "id": comment.id,
                "comment_author": comment.author.username,
                "comments_content": comment.content,
                "created_at": comment.created_at,
            }
            user_info["comments"].append(comment_info)

        return json.dumps(user_info, indent=4)

    def delete_user_by_email(self, user_email: str):
        user_to_deleting = self.db_conn.session.query(User).filter_by(
            email=user_email
        ).first()

        self.db_conn.session.delete(user_to_deleting)
        self.db_conn.commit_changes()

    def create_post(self, title: str, content: str):
        new_post = Post(
            title=title,
            content=content,
            author_id=self.get_user_id_by_email(
                input("Enter your email: ")
            ),
            created_at=get_datetime_string()
        )

        self.db_conn.session.add(new_post)
        self.db_conn.commit_changes()

    def create_comment(self, content: str, post_id: int):
        post = self.db_conn.session.query(Post).filter_by(
            id=post_id
        ).first()

        if post:
            new_comment = Comment(
                content=content,
                author_id=self.get_user_id_by_email(
                    input("Enter your email: ")
                ),
                post_id=post_id,
                created_at=get_datetime_string()
            )
            self.db_conn.session.add(new_comment)
            self.db_conn.commit_changes()
        else:
            raise sqlalchemy.exc.ConstraintColumnNotFoundError
