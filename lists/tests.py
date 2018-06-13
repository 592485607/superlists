from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page

# class SmokeTest(TestCase):
#     def test_bad_maths(self):
#         self.assertEqual(1+1,3)

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        #resolve 是 Django 内部使用的函数，用于解析 URL，并将其映射到相应的视图函数上。
        found = resolve('/')

        #检查解析网站根路径“/” 时，是否能找到名为 home_page 的函数
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        # 创建了一个 HttpRequest 对象，用户在浏览器中请求网页时， Django 看到的就是HttpRequest 对象
        request = HttpRequest()

        #把这个 HttpRequest 对象传给 home_page 视图，得到响应.
        response = home_page(request)

        #希望响应以 <html> 标签开头，并在结尾处关闭该标签。
        #注意：response.content 是原始字节，不是 Python 字符串，因此对比时要使用 b'' 句法
        self.assertTrue(response.content.startswith(b'<html>')) #➌
        self.assertIn(b'<title>To-Do lists</title>', response.content) #➍
        self.assertTrue(response.content.endswith(b'</html>'))