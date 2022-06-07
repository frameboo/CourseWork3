import json

class PostsDAO:

    def __init__(self, path):
        self.path = path

    def load_data(self):
        """загружает посты из posts.json"""
        with open(self.path, "r", encoding="utf-8") as file:
            return json.load(file)

    def get_all(self):
        """Возвращает все посты"""
        return self.load_data()

    def get_posts_by_user(self, user_name):
        """возвращает посты определенного пользователя"""
        posts = self.load_data()
        post_by_user = []

        for post in posts:
            if post["poster_name"] == user_name:
                post_by_user.append(post)
        return post_by_user

    def get_comments_by_pk(self, post_id):
        """возвращает комментарии определенного поста"""
        pass

    def search_for_posts(self, query):
        """возвращает список постов по ключевому слову"""
        posts = self.get_all()
        matching_post = []

        query_lower = query.lower()

        for post in posts:
            if query_lower in post["content"].lower():
                matching_post.append(post)
        return matching_post

    def get_post_by_pk(self, pk):
        """возвращает один пост по его идентификатору"""
        posts = self.get_all()

        for post in posts:
            if post["pk"] == pk:
                return post
        raise ValueError