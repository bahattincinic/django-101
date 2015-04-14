from django.conf.urls import url

from .views import SpeakerListView, SpeakerDetailView

urlpatterns = [
    url(r'^list/$', SpeakerListView.as_view(),
        name='speaker-list'),
    url(r'^detail/(?P<pk>[0-9]+)/$', SpeakerDetailView.as_view(),
        name='speaker-detail'),
]
