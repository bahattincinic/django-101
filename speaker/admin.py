from django.contrib import admin

from .models import Speaker


class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email',)
    search_fields = ['first_name', 'last_name', 'email']

admin.site.register(Speaker, SpeakerAdmin)
