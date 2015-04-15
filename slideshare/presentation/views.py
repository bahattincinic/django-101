from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.detail import SingleObjectMixin

from .models import Presentation, Category
from speaker.models import Speaker


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['speakers'] = Speaker.objects.order_by('-id')[:10]
        context['presentations'] = Presentation.objects.order_by('-id')[:10]
        return context


class PresentationDetailView(DetailView):
    model = Presentation
    template_name = 'presentation/detail.html'


class PresentationListView(ListView):
    model = Presentation
    template_name = 'presentation/list.html'


class CategoryDetailView(SingleObjectMixin, ListView):
    paginate_by = 12
    template_name = 'presentation/category_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Category.objects.all())
        return super(CategoryDetailView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context['object'] = self.object
        return context

    def get_queryset(self):
        return self.object.presentation_set.all()
