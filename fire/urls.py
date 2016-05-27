from django.conf.urls import url, patterns

from . import views

urlpatterns = [
    url(r'^(?P<id>\d+)/$', views.question_detail, name='fire_question-detail'),
]

