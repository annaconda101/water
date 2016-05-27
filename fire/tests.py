from django.test import TestCase
from .models import Question

class QuestionModelTest(TestCase):
    def test_string_representation(self):
        question = Question(title="When is the mother's day?")
        self.assertEqual(str(question), question.title)


class ProjectTests(TestCase):
    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
