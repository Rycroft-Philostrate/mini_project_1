import unittest
from utils import search_for_posts


class TestSearchForPosts(unittest.TestCase):
	"""Тесты поиска постов"""
	def test_query_posts(self):
		"""Проверка что находтся пост по ключевому слову"""
		data = search_for_posts('ПиРог')
		self.assertEqual(data[0]['pk'], 1)


if __name__ == '__main__':
	unittest.main()
