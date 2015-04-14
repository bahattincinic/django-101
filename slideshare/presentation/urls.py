from django.conf.urls import url

from .views import (PresentationDetailView, PresentationListView,
                    CategoryDetailView)

urlpatterns = [
    url(r'^list/$', PresentationListView.as_view(),
        name='presentation-list'),
    url(r'^detail/(?P<pk>[0-9]+)/$', PresentationDetailView.as_view(),
        name='presentation-detail'),
    url(r'^category/(?P<pk>[0-9]+)/$', CategoryDetailView.as_view(),
        name='category-detail'),
]
