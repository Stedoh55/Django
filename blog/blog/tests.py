from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Post
from django.urls import reverse # new

# Create your tests here.
class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="secret"
        )

        cls.post = Post.objects.create(
            title="A good title",
            body="Nice body content",
            author=cls.user,
        )
    
    def test_post_model(self):
        self.assertEqual(self.post.title, "A good title")               #1 Checking for database post title data
        self.assertEqual(self.post.body, "Nice body content")           #2 Checking for database post body data
        self.assertEqual(self.post.author.username, "testuser")         #3 Checking for database user data
        self.assertEqual(str(self.post), "A good title")                #4 Checking for database post title data entry description 
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")      #5 Checking for database post data index

    #6 Checking for Home Url
    def test_url_exists_at_correct_location_listview(self):             
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    #7 Checking for detailed view url
    def test_url_exists_at_correct_location_detailview(self):           
        response = self.client.get("/post/1/")
        self.assertEqual(response.status_code, 200)

    #8 Checking for the contents in the template for home
    def test_post_listview(self): # new
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)                        #Checking if the name of home url exists
        self.assertContains(response, "Nice body content")                 #Checking if contents of the home url is the model items
        self.assertTemplateUsed(response, "blog/home.html")                #checking if the used template is correct

    #9 Checking for the contents in the template for home
    def test_post_detailview(self): # new
        response = self.client.get(reverse("post_detail",kwargs={"pk": self.post.pk}))
        no_response = self.client.get("/post/100000/")

        self.assertEqual(response.status_code, 200)                        #Checking if the blog detail of  url exists with valid primary key
        self.assertEqual(no_response.status_code, 404)                     #Checking if the blog details return not found error when pk is invalid
        self.assertContains(response, "A good title")                      #Checking if contents of the blog details url is the model items
        self.assertTemplateUsed(response, "blog/post_detail.html")         #checking if the used template is correct       
