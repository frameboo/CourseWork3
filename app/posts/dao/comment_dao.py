import json


class CommentDAO:

    def __init__(self, path):
        self.path = path

    def load_data(self):
        """загружает комментарии из comments.json"""
        with open(self.path, "r", encoding="utf-8") as file:
            return json.load(file)

    def get_all(self):
        """Возвращает все комментарии"""
        return self.load_data()

    def get_comments_by_post(self, pk):
        """возвращает комментарии определенного поста"""
        comments = self.get_all()
        matching_comment = []
        for comment in comments:
            if comment["post_id"] == pk:
                matching_comment.append(comment)
        return matching_comment
