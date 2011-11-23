from django.shortcuts import get_object_or_404, render_to_response
from project.app.notes.models import Note

def view (request, id):
    note = get_object_or_404(Note,pk=id)
    return render_to_response('base.html',{'note':note})