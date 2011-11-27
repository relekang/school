from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from core.tags.models import Tag

class TagAdmin (ModelAdmin):
    model = Tag
    exclude = ('creator', 'saved_by', 'date_created', 'date_saved',)
admin.site.register(Tag,TagAdmin)