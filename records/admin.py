from django.contrib import admin

from .models import Topic, Note, Excerpts
# Register your models here.
admin.site.register(Topic)
admin.site.register(Note)
admin.site.register(Excerpts)