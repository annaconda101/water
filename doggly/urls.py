from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.fact_list, name='doggly-fact-list'),
]
