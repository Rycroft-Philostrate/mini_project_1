import unittest
from utils import get_comments_by_post_id


class TestGetCommentsByPostId(unittest.TestCase):
	"""Тесты получения комментраиев по id поста"""
	def test_not_id(self):
		"""Проверка когда поста с таким id не существует"""
		self.assertEqual(get_comments_by_post_id(56), ValueError)

	def test_post_id(self):
		"""Проверка когда есть пост c таким id"""
		post_id = get_comments_by_post_id(1)
		self.assertEqual(post_id[0]['comment'], "Очень здорово!")


if __name__ == '__main__':
	unittest.main()
