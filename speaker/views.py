from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Speaker


class SpeakerDetailView(DetailView):
    model = Speaker
    template_name = 'speaker/detail.html'


class SpeakerListView(ListView):
    model = Speaker
    template_name = 'speaker/list.html'
    paginate_by = 12
