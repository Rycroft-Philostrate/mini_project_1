from flask import Flask, render_template, request, redirect
from utils import *
from err_app import err
from api_app import api

app = Flask(__name__)
app.register_blueprint(err)
app.register_blueprint(api)


@app.route('/')
def index():
    """Главная страница все посты"""
    count_bookmarks = len(get_bookmark())
    return render_template('index.html', posts=get_posts_all(), count_bookmarks=count_bookmarks)


@app.route('/posts/<int:post_id>')
def post_page(post_id):
    """Представление поста по id"""
    post = get_post_by_pk(post_id)
    for element in post['content'].split():
        if element.startswith('#'):
            post['content'] = post['content'].replace(element, f'<a href="/tag/{element[1:]}" class="item__tag">{element}</a>', 1)
    return render_template('post.html', post=post, comments=get_comments_by_post_id(post_id),
                           count_comments=correct_word_comments(post_id))


@app.route('/search/')
def search():
    """Поиск постов по ключевому слову"""
    query = request.values.get('s')
    return render_template('search.html', find_posts=search_for_posts(query))


@app.route('/users/<username>')
def user_feed(username):
    """Посты пользователя"""
    return render_template('user-feed.html', user_posts=get_posts_by_user(username))


@app.route('/tag/<tagname>')
def tag_page(tagname):
    """Посты по тэгу"""
    return render_template('tag.html', tagname=tagname, posts=find_tag(tagname))


@app.route('/bookmarks')
def bookmark():
    return render_template('bookmarks.html', posts=get_bookmark())


@app.route('/bookmark/add/<int:post_id>', methods=['GET'])
def add_post_bookmark(post_id):
    """Добавления поста в закладки"""
    add_bookmark(post_id)
    return redirect('/', code=302)


@app.route('/bookmark/remove/<int:post_id>')
def remove_post_bookmark(post_id):
    """Удаления поста из закладок"""
    remove_bookmark(post_id)
    return redirect('/', code=302)


if __name__ == '__main__':
    app.run()
