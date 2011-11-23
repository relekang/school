from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from app.notes.models import Course
from project.app.notes.models import Note

class CourseAdmin (ModelAdmin):
    model = Course
    exclude = ('creator', 'saved_by', 'date_created', 'date_saved',)
admin.site.register(Course,CourseAdmin)

class NoteAdmin (ModelAdmin):
    model = Note
    exclude = ('creator', 'saved_by', 'date_created', 'date_saved',)
admin.site.register(Note,NoteAdmin)

