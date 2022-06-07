import json


class BookmarksDAO:

    def __init__(self, path):
        self.path = path

    def load_data(self):
        """загружает закладки из bookmarks.json"""
        with open(self.path, "r", encoding="utf-8") as file:
            return json.load(file)

    def get_all(self):
        """Возвращает все закладки"""
        return self.load_data()

    def get_by_pk(self, pk):
        """возвращает закладку по pk"""
        bookmarks = self.load_data()
        for bookmark in bookmarks:
            if bookmark["pk"] == pk:
                return bookmark

    def add_bookmark(self, posts):
        """добавляет пост"""
        with open(self.path, "w+", encoding="utf-8") as file:
            json.dump(posts, file, ensure_ascii=False)

    def is_exists_post(self, post):
        """проверяет существует ли такой пост в закладках"""
        bookmarks = self.get_all()

        for bookmark in bookmarks:
            if post == bookmark:
                return True
        return False

    def delete_bookmark(self, post):
        bookmarks = self.get_all()
        new_bookmarks = []

        for bookmark in bookmarks:
            if post != bookmark:
                new_bookmarks.append(bookmark)

        with open(self.path, "w+", encoding="utf-8") as file:
            json.dump(new_bookmarks, file, ensure_ascii=False)

    def get_all_pk(self):
        bookmarks = self.get_all()
        pk_list = []
        for bookmark in bookmarks:
            pk_list.append(bookmark["pk"])
        return pk_list

