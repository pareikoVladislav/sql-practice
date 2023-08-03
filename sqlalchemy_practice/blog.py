from db_conn import Database
from users import UserManager
from posts import PostsManager
from comments import CommentsManager


class Blog:
    def __init__(self):
        self.db_conn = Database()
        self.users = UserManager()
        self.posts = PostsManager()
        self.comments = CommentsManager()

    @staticmethod
    def print_choices():
        return """
        add new user | update username | get user by id
        get all users | delete user | create post | leave comment
        get post by id | update post title | delete post
        get all comments | get comment by id | update comment
        delete comment
        """

    def main(self):
        while True:
            print(self.print_choices())
            user_choice = input("Enter action, you needed: ")
            match user_choice:
                case "q":
                    self.db_conn.close_connection()
                    break
                case "add new user":
                    self.users.create_new_user(
                        input("Enter a username: "),
                        input("Enter a password: "),
                        input("Enter email: "),
                        input("Provide some info about you: "),
                    )
                case "update username":
                    self.users.update_username_by_email(
                        input("Enter you email: ")
                    )
                case "get user by id":
                    print(self.users.get_user_by_id(
                        int(input("Enter user ID: "))
                    ))
                case "get all users":
                    print(self.users.get_all_users())
                case "delete user":
                    self.users.delete_user_by_email(
                        input("Enter user's email: ")
                    )
                case "create post":
                    self.users.create_post(
                        input("Enter a post's title: "),
                        input("Enter a content to this post: ")
                    )
                case "leave comment":
                    self.users.create_comment(
                        input("Enter your comment: "),
                        int(input("Enter a post ID for this comment: "))
                    )
                case "get post by id":
                    print(self.posts.get_post_by_id(
                        int(input("Enter a post ID: "))
                    ))
                case "update post title":
                    self.posts.update_post_title(
                        int(input("Enter a post ID: "))
                    )
                case "delete post":
                    self.posts.delete_post(
                        int(input("Enter a post ID: "))
                    )
                case "get all comments":
                    print(self.comments.get_all_comments())
                case "get comment by id":
                    print(self.comments.get_comment_by_id(
                        int(input("Enter a comment ID: "))
                    ))
                case "update comment":
                    self.comments.update_comment(
                        int(input("Enter a comment ID: "))
                    )
                case "delete comment":
                    self.comments.delete_comment(
                        int(input("Enter a comment ID: "))
                    )
                case _:
                    print("Sorry, I don't know this operation. Please, try again.")


if __name__ == "__main__":
    blog = Blog()
    blog.main()
