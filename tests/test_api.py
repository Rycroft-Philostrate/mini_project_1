import unittest
import requests


class TestApi(unittest.TestCase):
	"""Тесты api"""
	def test_api_posts_list(self):
		"""Проверка что возвращается список, у элементов есть нужные ключи"""
		response = requests.get('http://127.0.0.1:5000/api/posts').json()
		self.assertEqual(type(response), list)
		self.assertIn('pk', response[0])
		self.assertIn('poster_name', response[0])
		self.assertIn('content', response[0])

	def test_api_post_id(self):
		"""Проверка что возвращается словарь с нужными ключами"""
		response = requests.get('http://127.0.0.1:5000/api/posts/?s=2').json()
		self.assertEqual(type(response), dict)
		self.assertIn('poster_name', response)
		self.assertIn('pk', response)
		self.assertIn('content', response)


if __name__ == '__main__':
	unittest.main()
