import unittest
from utils import find_tag


class TestFindTag(unittest.TestCase):
	"""Тесты поиска постов по тэгу"""
	def test_find_tag(self):
		"""Проверка что по существующему тэгу находятся посты"""
		self.assertGreater(len(find_tag('кот')), 0)
		self.assertEqual(type(find_tag('кот')), list)


if __name__ == '__main__':
	unittest.main()
