from django.test import SimpleTestCase
from django.urls import reverse, resolve
from testapp.views import user_login, get_all_user

class TestUrls(SimpleTestCase):

    def test_userlogin_url_resolves(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, user_login)

    def test_alluser_url_resolves(self):
        url = reverse('all_user')
        self.assertEquals(resolve(url).func, get_all_user)
