from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class BaseTest(TestCase):
    def setUp(self):
        self.home_url = reverse('home')
        self.register_url=reverse('signup')
        self.login_url=reverse('signin')
        self.user={
            'username':'username',
            'password':'password',
            'password2':'password',
        }
        return super().setUp()

class HomeTest(BaseTest):
    def test_can_view_page_correctly(self):
        response=self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/home.html')

class RegisterTest(BaseTest):
   def test_can_view_page_correctly(self):
       response=self.client.get(self.register_url)
       self.assertEqual(response.status_code,200)
       self.assertTemplateUsed(response,'authentication/register.html')

   def test_can_register_user(self):
        response=self.client.post(self.register_url,self.user,format='text/html')
        self.assertEqual(response.status_code,200)

class LoginTest(BaseTest):
    def test_can_access_page(self):
        response=self.client.get(self.login_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'authentication/login.html')

    def test_login_success(self):
        response= self.client.post(self.login_url,self.user,format='text/html')
        self.assertEqual(response.status_code,200)