import unittest
from utils import get_posts_all, get_comments_all, get_bookmark


class TestGetJson(unittest.TestCase):
	"""Тесты загрузи данных из json файлов"""
	def test_get_posts(self):
		"""Проверка получения данных из data.json в виде списка"""
		self.assertEqual(type(get_posts_all()), list)

	def test_get_comments(self):
		"""Проверка получения данных из comments.json в виде списка"""
		self.assertEqual(type(get_comments_all()), list)

	def test_get_bookmark(self):
		"""Проверка получения закладок"""
		self.assertEqual(type(get_bookmark()), list)


if __name__ == '__main__':
	unittest.main()
