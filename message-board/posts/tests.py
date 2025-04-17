from django.test import TestCase
from django.urls import reverse
from .models import Post

# Create your tests here.
class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a test!")

    #1 Testing for Data Stored in the database
    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test!")

    #2 checking if the path "/" exists at the url patterns
    def test_url_exists_at_correct_location(self): # new
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    #3 Checking if the name "home" is accessed by the url patterns name
    def test_url_available_by_name(self): # new
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    #4 Checking for the use of the correct template name
    def test_template_name_correct(self): # new
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "posts/home.html")
    
    #5 Checking if Template returns the data from the Database
    def test_template_content(self): # new
        response = self.client.get(reverse("home"))
        self.assertContains(response, "This is a test!")

    ################################################################

        #   ALTERNATIVE     # Using Unittest for Tests 3 to 5

    ################################################################
    def test_homepage(self):
        response = self.client.get(reverse("home"))

        # Colecting All test cases
        self.assertEqual(response.status_code, 200)                 #Test 3
        self.assertTemplateUsed(response, "posts/home.html")        #Test 4
        self.assertContains(response, "This is a test!")            #Test 5