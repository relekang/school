from django.forms.models import ModelForm
from app.notes.models import Note

class NoteForm (ModelForm):
    class Meta:
        model = Note
        exclude = ('creator', 'saved_by', 'date_created', 'date_saved','course')