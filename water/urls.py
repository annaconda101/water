from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^fire/', include('fire.urls')),
    url(r'^admin/', admin.site.urls),
]
