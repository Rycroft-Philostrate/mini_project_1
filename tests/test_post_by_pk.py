import unittest
from utils import get_post_by_pk


class TestPostByPk(unittest.TestCase):
	"""Тесты проверки получения поста id"""
	def test_post_pk(self):
		"""Проверка получения поста по существующему id"""
		self.assertEqual(get_post_by_pk(2)['poster_name'], "johnny")

	def test_not_post(self):
		"""Проверка если не существует поста по данному id"""
		self.assertEqual(get_post_by_pk(56), ValueError)


if __name__ == '__main__':
	unittest.main()
