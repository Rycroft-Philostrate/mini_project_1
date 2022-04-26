import unittest
from utils import get_posts_by_user


class TestGetPostByUser(unittest.TestCase):
	"""Тесты получения постов пользователя"""
	def test_user_posts(self):
		"""Провека что посты конкретного пользователя находятся"""
		data = get_posts_by_user('Johnny')
		self.assertGreater(len(data), 1)

	def test_not_user(self):
		"""Проверка если не существует пользователя"""
		self.assertEqual(get_posts_by_user('HHHHH'), ValueError)

	def test_not_post(self):
		"""Проверка если нет постов для существующего пользователя"""
		pass


if __name__ == '__main__':
	unittest.main()
