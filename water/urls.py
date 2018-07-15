from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^', include('fire.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^doggly', include('doggly.urls')),
]
