from django.forms.models import ModelForm
from app.notes.models import Note
from django import forms

class NoteForm (ModelForm):
    tags = forms.CharField(required=False)
    class Meta:
        model = Note
        exclude = ('creator', 'saved_by', 'date_created', 'date_saved','course')