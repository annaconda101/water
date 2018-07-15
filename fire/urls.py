from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<id>\d+)/$', views.question_detail, name='fire_question-detail'),
    url(r'^new/$', views.question_create, name='fire_question-new'),

    url(r'^(?P<id>\d+)/upvote_answer/$', views.answer_upvote, name='fire_answer-upvote'),
    url(r'^(?P<id>\d+)/downvote_answer/$', views.answer_downvote, name='fire_answer-downvote'),
]

