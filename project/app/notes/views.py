from django.shortcuts import get_object_or_404, render_to_response
from app.notes.models import Course
from project.app.notes.models import Note

def list (request, course=None):
    if course:
        course = get_object_or_404(Course, code=course)
        notes = Note.objects.filter(course=course)
        courses = None
    else:
        notes = None
        courses = Course.objects.all()
    return render_to_response('notes/base.html',
                             {'notes': notes,
                              'courses': courses})

def view (request, id):
    note = get_object_or_404(Note,pk=id)
    return render_to_response('notes/view.html',
                             {'note': note})