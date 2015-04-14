from django.contrib import admin

from .models import Presentation, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']


class PresentationAdmin(admin.ModelAdmin):
    list_display = ('title', 'speaker',)
    list_filter = ('categories',)
    search_fields = ['title']
    filter_horizontal = ('categories',)

admin.site.register(Presentation, PresentationAdmin)
admin.site.register(Category, CategoryAdmin)
