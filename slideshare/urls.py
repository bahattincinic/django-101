from django.conf.urls import include, url
from django.contrib import admin

from presentation.views import HomeView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^speaker/', include('speaker.urls')),
    url(r'^presentation/', include('presentation.urls')),
]
