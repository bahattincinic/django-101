from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Speaker


class SpeakerDetailView(DetailView):
    model = Speaker


class SpeakerListView(ListView):
    model = Speaker
