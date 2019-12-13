from django.test import TestCase

class SimpleTest(TestCase):
    def setUp(self):
        user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')

    def test_secure_page(self):
        c = Client()
        print c.login(username='temporary', password='temporary')
        response = c.get('/users/', follow=True)
        user = User.objects.get(username='temporary')
        self.assertEqual(response.context['email'], 'temporary@gmail.com')

    def test_true_is_true(self):
        """Tests that True equals True"""
        self.assertEqual(True, True)

class PageDetailView_Test(TestCase):
    """Tests that the Detail Page works."""
    def test_detail_page(self):
        #Create a user for this test 
        user = User.objects.create()

        #Create a page to the database 
        Page.objects.create(title="My Test Page", content="test", author=user)


        #Make a GET request, and test route returns 200
        reponse = self.client.get("/my-test-page/")

        self.assertEqual(reponse.status_code, 200)