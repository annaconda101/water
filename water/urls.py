from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^fire/', include('fire.urls')),
    url(r'^admin/', admin.site.urls),
]
