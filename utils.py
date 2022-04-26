import json


def get_posts_all():
	"""Возврашает все посты"""
	with open('data.json', encoding='utf-8') as file:
		return json.load(file)


def get_comments_all():
	"""Возврашает все комментарии"""
	with open('comments.json', encoding='utf-8') as file:
		return json.load(file)


def get_posts_by_user(user_name):
	"""Возврашает все посты пользователя"""
	user_posts = []
	for post in get_posts_all():
		if user_name.lower() == post['poster_name'].lower():
			user_posts.append(post)
	if not user_posts:
		return ValueError
	else:
		return user_posts


def get_comments_by_post_id(post_id):
	"""Возврашает все комментарии поста по id"""
	list_comments = []
	list_id = [post['pk'] for post in get_posts_all()]
	if post_id not in list_id:
		return ValueError
	else:
		for comment in get_comments_all():
			if post_id == comment['post_id']:
				list_comments.append(comment)
	return list_comments


def search_for_posts(query):
	"""Возврашает посты по ключевому слову"""
	list_post = []
	if query is None:
		return list_post
	for post in get_posts_all():
		if query.lower() in post['content'].lower():
			list_post.append(post)
	return list_post


def get_post_by_pk(pk):
	"""Возврашает пост по id"""
	for post in get_posts_all():
		if int(pk) == post['pk']:
			return post
	else:
		return ValueError


def correct_word_comments(post_id):
	"""Корректировка слова 'комментарий'"""
	count_comments = len(get_comments_by_post_id(post_id))
	if count_comments % 10 == 1 and count_comments != 11:
		return f'{count_comments} комментарий'
	elif count_comments % 10 in (2, 3, 4) and count_comments not in (12, 13, 14):
		return f'{count_comments} комментария'
	else:
		return f'{count_comments} комментариев'


def find_tag(tagname):
	"""Поиск постов по тэгу"""
	tag_posts = []
	posts = get_posts_all()
	for post in posts:
		if f'#{tagname}' in post['content'].split():
			tag_posts.append(post)
	return tag_posts


def get_bookmark():
	"""Возвращает все закладки"""
	with open('bookmarks.json', encoding='utf-8') as file:
		return json.load(file)


def add_bookmark(post_id):
	"""Запись данных поста в файл закладок"""
	posts_bookmarks = get_bookmark()
	list_id_bookmark = [pk['pk'] for pk in posts_bookmarks]  # список id постов в закладках
	with open('bookmarks.json', 'w', encoding='utf-8') as file:
		for post in get_posts_all():
			if post_id == post['pk']:
				if post_id in list_id_bookmark:  # если пост уже есть в закладках не добавляется повторно
					break
				posts_bookmarks.append(post)
				break
		json.dump(posts_bookmarks, file, indent=2, ensure_ascii=False)


def remove_bookmark(post_id):
	"""Удаление постов из закладок"""
	posts_bookmarks = get_bookmark()
	with open('bookmarks.json', 'w', encoding='utf-8') as file:
		for post in posts_bookmarks:
			if post_id == post['pk']:
				posts_bookmarks.remove(post)
				break
		json.dump(posts_bookmarks, file, indent=2, ensure_ascii=False)
