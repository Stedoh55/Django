from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class SignupPageTests(TestCase):
    # Testing for the signup url
    def test_url_exists_at_correct_location_signupview(self):
        response = self.client.get("/accounts/signup")
        self.assertEqual(response.status_code, 200)

    # Testing for the signup url page name
    def test_signup_view_name(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")

    # Testing for the form data on signup
    def test_signup_form(self):
        response = self.client.post(
        reverse("signup"),
            {
            "username": "testuser",
            "email": "testuser@email.com",
            "password1": "testpass123",
            "password2": "testpass123",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, "testuser")
        self.assertEqual(get_user_model().objects.all()[0].email, "testuser@email.com")
