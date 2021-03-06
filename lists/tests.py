from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page
from django.http import HttpRequest

class HomePageTest(TestCase):
	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_return_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		expected_html = render_to_string('home.html')
		self.assertEqual(response.content.decode(),expected_html)


	def test_home_page_can_save_a_Post_request(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['item_text'] = 'A new list item' #设置配置

		response = home_page(request) #测试函数
		self.assertIn('A new list item', response.content.decode()) #编写断言
		expected_html = render_to_string('home.html',{'new_item_text': 'A new list item'})
		self.assertEqual(response.content.decode(), expected_html)
		# self.assertTrue(response.content.startswith(b'<html>'))
		# self.assertIn(b'<title>To-Do lists</title>', response.content)
		# self.assertTrue(response.content.strip().endswith(b'</html>'))
