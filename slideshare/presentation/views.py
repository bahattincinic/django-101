from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Presentation, Category
from speaker.models import Speaker


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['speakers'] = Speaker.objects.all()[:10]
        context['presentations'] = Presentation.objects.all()[:10]
        return context


class PresentationDetailView(DetailView):
    model = Presentation


class PresentationListView(ListView):
    model = Presentation


class CategoryDetailView(DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context['presentations'] = self.object.presentation_set.all()
        return context
