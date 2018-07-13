from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django_webtest import WebTest

from .models import Question, Answer
from .forms import AnswerForm, QuestionForm

from mock import patch


class QuestionModelTest(TestCase):
    def test_string_representation(self):
        question = Question(title="When is the mother's day?")
        self.assertEqual(str(question), question.title)


class ProjectTests(TestCase):
    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


class HomePageTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username='some_user')

    def test_one_question(self):
        title = 'Where is the best place to get ramen in Sydney CBD?'
        description = 'One for the foodies.'
        Question.objects.create(title=title, description=description)
        response = self.client.get('/')
        self.assertContains(response, title)
        self.assertContains(response, description)

    def test_two_questions(self):
        first_title = 'Where is the best place to get ramen in Sydney CBD?'
        first_description = 'One for the foodies.'
        second_title = 'Why is it important to manage your time?'
        second_description = 'Time management'
        Question.objects.create(title=first_title, description=first_description)
        Question.objects.create(title=second_title, description=second_description)
        response = self.client.get('/')
        self.assertContains(response, first_title)
        self.assertContains(response, first_description)
        self.assertContains(response, second_title)
        self.assertContains(response, second_description)

    def test_create_new_question_url(self):
        response = self.client.get(reverse('fire_question-new'))
        self.assertEqual(response.status_code, 200)

    def test_new_question_url_on_homepage(self):
        response = self.client.get('/')
        new_question_url = self.client.get(reverse('fire_question-new')).request['PATH_INFO']
        self.assertContains(response, new_question_url)


class QuestionViewTest(WebTest):
    def setUp(self):
        self.user = get_user_model().objects.create(username='some_user')
        self.question = Question.objects.create(title='Android or iPhone?', description='Help a non-techy person out!')
        text = 'I am using Android now, but missing some iPhone features.'
        self.answer = Answer.objects.create(text=text, question=self.question, sentiment_polarity=0.00)

    def test_basic_view(self):
        response = self.client.get(self.question.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_question_and_answer_relationship(self):
        number_of_answers = len(self.question.answers.all())
        self.assertEqual(number_of_answers, 1)

    def test_view_with_one_answer(self):
        response = self.client.get(self.question.get_absolute_url())
        self.assertContains(response, str(self.answer.text))

    def test_view_page(self):
        page = self.app.get(self.question.get_absolute_url())
        self.assertEqual(len(page.forms), 1)

    def test_form_error(self):
        page = self.app.get(self.question.get_absolute_url())
        page = page.form.submit()
        self.assertContains(page, "This field is required.")

    def test_form_success(self):
        page = self.app.get(self.question.get_absolute_url())
        page.form['text'] = "Test answer"
        page = page.form.submit()
        self.assertRedirects(page, self.question.get_absolute_url())

    def test_upvoting_answer(self):
        question = Question.objects.create(title='Android or iPhone?', description='Help a non-techy person out!')
        text = 'I am using Android now, but missing some iPhone features.'
        answer = Answer.objects.create(text=text, question=question, score=0, sentiment_polarity=0.00)

        question_detail_response = self.app.get(reverse('fire_question-detail', kwargs={'id':question.id}))
        answer_downvote_response = question_detail_response.click(linkid='answer-%s-upvote' %answer.id)
        answer_score = answer_downvote_response.follow().html.select('#answer-%s-score' %answer.id)
        answer_score_text = answer_downvote_response.follow().html.select('#answer-%s-score' %answer.id)[0].text

        self.assertEqual(answer_score_text, u'votes: 1')

    def test_downvoting_answer(self):
        question = Question.objects.create(title='Android or iPhone?', description='Help a non-techy person out!')
        text = 'I am using Android now, but missing some iPhone features.'
        answer = Answer.objects.create(text=text, question=question, score=0, sentiment_polarity=0.00)

        question_detail_response = self.app.get(reverse('fire_question-detail', kwargs={'id':question.id}))
        answer_downvote_response = question_detail_response.click(linkid='answer-%s-downvote' %answer.id)
        answer_score = answer_downvote_response.follow().html.select('#answer-%s-score' %answer.id)
        answer_score_text = answer_downvote_response.follow().html.select('#answer-%s-score' %answer.id)[0].text

        self.assertEqual(answer_score_text, u'votes: -1')


class AnswerModelTest(TestCase):

    def test_string_representation(self):
        text = 'I personally like Android.'
        answer = Answer(text=text)
        self.assertEqual(str(answer), text)

    def test_score_defaults_to_zero(self):
        text = 'I personally like Android.'
        answer = Answer(text=text)
        self.assertEqual(answer.score, 0)


class AnswerFormTest(TestCase):

    def setUp(self):
        user = get_user_model().objects.create_user('annav')
        self.question = Question.objects.create(title="What's your favourite flavour of tea", description='I like drinks!')

    def test_init(self):
        AnswerForm(question=self.question)

    def test_init_without_question(self):
        with self.assertRaises(KeyError):
            AnswerForm()

    def test_valid_data(self):
        form = AnswerForm(
            {'text': "Sample answer",},
            question=self.question
        )
        self.assertTrue(form.is_valid())
        answer = form.save()
        self.assertEqual(answer.text, "Sample answer")

    def test_blank_data(self):
        form = AnswerForm({}, question=self.question)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'text': ['This field is required.'],
     })


class QuestionFormTest(WebTest):
    def setUp(self):
        user = get_user_model().objects.create_user('annav')

    def test_init(self):
        QuestionForm()

    def test_valid_data(self):
        sample_title = "Describe what to you is the best holiday?"
        sample_description = "Daydreaming of my next break..."
        form = QuestionForm({
            'title': sample_title,
            'description': sample_description,
        })
        self.assertTrue(form.is_valid())
        question = form.save()
        self.assertEqual(question.title, sample_title)
        self.assertEqual(question.description, sample_description)

    def test_blank_data(self):
        form = QuestionForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'title': ['This field is required.'],
            'description': ['This field is required.'],
     })

    def test_view_page(self):
        new_question_page = self.app.get(reverse('fire_question-new'))
        self.assertEqual(len(new_question_page.forms), 1)

    def test_form_error(self):
        new_question_page = self.app.get(reverse('fire_question-new'))
        page = new_question_page.form.submit()
        self.assertContains(page, "This field is required.")

    def test_form_success(self):
        new_question_page = self.app.get(reverse('fire_question-new'))
        title = "What are the continents of the world?"
        description = "an easy question"
        new_question_page.form['title'] = title
        new_question_page.form['description'] = description

        response = new_question_page.form.submit()

        self.assertEqual(response.status_code, 302)
        self.assertContains(response.follow(), title)
        self.assertContains(response.follow(), description)

