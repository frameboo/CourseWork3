import logging
import loggers

from flask import render_template, Blueprint, request, redirect, abort
from app.posts.dao.posts_dao import PostsDAO
from app.posts.dao.comment_dao import CommentDAO
from app.posts.dao.bookmarks_dao import BookmarksDAO
from app.config import *

posts_blueprint = Blueprint("posts_blueprint", __name__, template_folder="templates")
posts_dao = PostsDAO(POSTS_PATH)
comments_dao = CommentDAO(COMMENTS_PATH)
bookmarks_dao = BookmarksDAO(BOOKMARKS_PATH)

loggers.create_logger()
logger = logging.getLogger("basic")


@posts_blueprint.route("/")
def posts_all_page():
    """Страничка со всеми постами"""
    logger.debug("Запрошены все посты")
    try:
        posts = posts_dao.get_all()
        bookmarks = bookmarks_dao.get_all()
        bookmarks_count = len(bookmarks)
        bookmarks_pk = bookmarks_dao.get_all_pk()
        return render_template("index.html", posts=posts, bookmarks_count=bookmarks_count, bookmarks_pk=bookmarks_pk)
    except:
        return "Что-то пошло не так"


@posts_blueprint.route('/post/<int:post_pk>/')
def get_post_page(post_pk):
    """ Страничка поста полученного по post_pk """
    logger.debug(f"Запрошен пост {post_pk}")
    try:
        post = posts_dao.get_post_by_pk(post_pk)

        if post is None:
            abort(404)
        comments = comments_dao.get_comments_by_post(post_pk)
        comments_count = len(comments)
        return render_template("post.html", post=post, comments=comments, comments_count=comments_count)
    except ValueError:
        return "Такой пост не найден"
    except:
        return "Что-то пошло не так"


@posts_blueprint.route('/userfeed/<poster_name>')
def user_feed_page(poster_name):
    """ Страничка постов человека с именем poster_name """
    logger.debug(f"Запрошены посты пользователя -> {poster_name}")
    try:
        posts = posts_dao.get_posts_by_user(poster_name)
        return render_template("user-feed.html", posts=posts)
    except:
        return "Что-то пошло не так"


@posts_blueprint.route('/search/')
def posts_search_page():
    """ Страничка поиска по словам в описании поста (content) """
    try:
        s = request.values.get('s')
        posts = posts_dao.search_for_posts(s)
        posts_count = len(posts)
        return render_template("search.html", posts=posts, posts_count=posts_count)
    except AttributeError:
        return render_template("search.html")


@posts_blueprint.route('/users/<username>/')
def posts_by_user_page(username):
    return "Поиск по пользователю"


@posts_blueprint.route('/bookmarks/')
def bookmarks_page():
    """ Страничка закладок """
    bookmarks = bookmarks_dao.get_all()
    return render_template("bookmarks.html", bookmarks=bookmarks)


@posts_blueprint.route('/bookmarks/add/<int:post_pk>/')
def bookmarks_add_page(post_pk):
    """ Страничка добавления поста в закладки """
    post = posts_dao.get_post_by_pk(post_pk)
    bookmarks = bookmarks_dao.get_all()
    if bookmarks_dao.is_exists_post(post):
        return redirect("/", code=302)
    bookmarks.append(post)
    bookmarks_dao.add_bookmark(bookmarks)
    return redirect("/", code=302)


@posts_blueprint.route('/bookmarks/remove/<int:post_pk>/')
def bookmarks_remove_page(post_pk):
    """ Страничка удаления поста из закладок """
    bookmark_del = bookmarks_dao.get_by_pk(post_pk)
    bookmarks_dao.delete_bookmark(bookmark_del)
    return redirect("/bookmarks/", code=302)


@posts_blueprint.app_errorhandler(404)
def page_not_found(e):
    return "Такой страницы не существует", 404


@posts_blueprint.app_errorhandler(500)
def page_not_found(e):
    return "Возникли какие-то проблемы на стороне сервера", 500
