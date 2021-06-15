from django.test import TestCase
from faker import Factory
from faker.utils.text import slugify

from core.models import Question
from django.contrib.auth.models import User

faker = Factory.create()


class TestQuestionModel(TestCase):

    def setUp(self):
        user = User.objects.create(username=faker.name(), email=faker.email(), password=faker.password())
        self.question = Question.objects.create(
            user=user,
            title=faker.text(max_nb_chars=10),
            body=faker.text(max_nb_chars=40),
        )

    def test_question_create(self):
        self.assertEqual(self.question.slug, slugify(self.question.title))
