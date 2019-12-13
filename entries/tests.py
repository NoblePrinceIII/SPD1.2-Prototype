from django.test import TestCase

class SimpleTest(TestCase):
    def setUp(self):
        user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')

    def test_secure_page(self):
        c = Client()
        print c.login(username='temporary', password='temporary')
        response = c.get('/users/secure/', follow=True)
        user = User.objects.get(username='temporary')
        self.assertEqual(response.context['email'], 'temporary@gmail.com')