from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from app.notes.models import Course
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
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
@login_required
def preview(request, id):
    return view(request, id, preview=True)

@login_required
def view (request, id, preview=False):
    note = get_object_or_404(Note,pk=id)
    return render_to_response('notes/view.html',
                             {'note': note,
                              'preview': preview})

@csrf_exempt
def timestamp (request):
    if request.method == 'POST':
        id = request.POST.get('note_id')
        timestamp = cache.get('notetimestamp' + id)
        if not timestamp:
            note = get_object_or_404(Note, pk=id)
            timestamp = datetime.strftime(note.date_saved, '%d.%m.%y %I:%M')
            cache.set('notetimestamp' + id, timestamp)
        return HttpResponse(timestamp)
    else:
        return HttpResponse(status=400)