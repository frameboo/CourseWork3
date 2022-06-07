import pytest

from app.posts.dao.comment_dao import CommentDAO
from app.config import *

class TestCommentDAO:

    @pytest.fixture()
    def comment_dao(self):
        return CommentDAO(COMMENTS_PATH)

    @pytest.fixture()
    def post_pk(self):
        parameters_to_get_by_pk = []
        for comment in CommentDAO(f"{COMMENTS_PATH}").get_all():
            parameters_to_get_by_pk.append(comment["post_id"])
        return parameters_to_get_by_pk

    def test_get_all_check_type(self, comment_dao):
        """ Проверка всех комментариев на правильность типов """
        comments = comment_dao.get_all()
        assert type(comments) == list, "Список комментариев должен быть списком"
        assert type(comments[0]) == dict, "Элемент списка комментариев должен быть словарём"
