import logging

from flask import Blueprint, jsonify
from app.posts.dao.posts_dao import PostsDAO
from app.config import *

api_blueprint = Blueprint("api_blueprint", __name__)

posts_dao = PostsDAO(POSTS_PATH)

logger = logging.getLogger("basic")

@api_blueprint.route('/api/posts/')
def posts_all():
    """ Возвращает все посты """
    logger.debug("Запрошены все посты")
    posts = posts_dao.get_all()
    return jsonify(posts)


@api_blueprint.route('/api/posts/<int:post_pk>/')
def get_post(post_pk):
    """ Возвращает пост по post_pk """
    logger.debug(f"Запрошен пост {post_pk}")
    posts = posts_dao.get_post_by_pk(post_pk)
    return jsonify(posts)
