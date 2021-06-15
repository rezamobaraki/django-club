from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from faker import Faker

from accounts.forms import UserRegistrationForm
from accounts.models import Profile

faker = Faker()


class TestView(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_user_register_GET(self) -> None:
        response = self.client.get(reverse('accounts:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')
        self.failUnless(response.context['form'], UserRegistrationForm)

    def test_user_register_POST_valid(self) -> None:
        """
        Acceptance Test
        :return: None
        """
        response = self.client.post(reverse('accounts:register'), data={
            'username': faker.name(),
            'email': faker.email(),
            'password': faker.password(),
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(Profile.objects.count(), 1)

    def test_user_register_post_invalid(self) :
        """
        Rejection Test
        :return: None
        """
        response = self.client.post(reverse('accounts:register'), data={
            'username': faker.name(),
            'email': 'invalid_email',
            'password': faker.password(),
        })

        self.assertEqual(response.status_code, 200)
        self.failIf(response.context['form'].is_valid())
        self.assertFormError(response, 'form', 'email', errors=['Enter a valid email address.'])

    def test_user_dashboard_GET(self):
        user_password = faker.password()
        user = User.objects.create_user(username=faker.name(), password=user_password, email=faker.email())
        self.client.login(username=user.username, password=user_password)
        response = self.client.get(reverse('accounts:dashboard', args=[user.username]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/dashboard.html')
