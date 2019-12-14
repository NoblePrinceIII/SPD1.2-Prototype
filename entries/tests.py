from django.test import TestCase

class PageDetailView_Test(TestCase):
    """Tests that the Detail Page works."""
    def test_detail_page(self):

        #Make a GET request, and test route returns 200
        reponse = self.client.get("/my-test-page/")

        self.assertEqual(reponse.status_code, 200)

    def test_true_is_true(self):
        """Tests that True equals True"""
        self.assertEqual(True, True)
