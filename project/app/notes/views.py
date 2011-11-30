from datetime import datetime
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template.context import RequestContext
from app.notes.forms import NoteForm
from app.notes.models import Course
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
from core.tags.models import Tag
from project.app.notes.models import Note

@login_required
def list (request, course=None):
    if course:
        course = get_object_or_404(Course, code=course)
        notes = Note.objects.filter(course=course)
        courses = None
    else:
        notes = None
        course = None
        courses = Course.objects.all()
    return render_to_response('notes/base.html',
                             {'notes': notes,
                              'course': course,
                              'courses': courses},
                              context_instance=RequestContext(request))
@login_required
def preview(request, id):
    return view(request, id, preview=True)

@login_required
def view (request, id, preview=False):
    note = get_object_or_404(Note,pk=id)
    return render_to_response('notes/view.html',
                             {'note': note,
                              'preview': preview},
                              context_instance=RequestContext(request))
@login_required
def add (request, course):
    return edit(request, course)

@staff_member_required
def edit (request, course=False, id=False):
    if id:
        note = get_object_or_404(Note,pk=id)
    else:
        course = get_object_or_404(Course,code=course)
        note = Note(course=course)
    form = NoteForm(instance=note)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save()
            for t in form.cleaned_data['tags']:
                tag = Tag.objects.get_or_create(title=t)[0]
                note.add_tag(tag)
    return render_to_response('notes/edit.html',
                             {'note': note,
                              'form': form},
                              context_instance=RequestContext(request))

@staff_member_required
def save (request, course=False, id=False):
    if request.method == 'POST':
        if id:
            note = get_object_or_404(Note,pk=id)
        else:
            course = get_object_or_404(Course,code=course)
            note = Note(course=course)
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save()
            for t in form.cleaned_data['tags']:
                tag = Tag.objects.get_or_create(title=t)[0]
                note.add_tag(tag)
    return HttpResponse('Saved')

@csrf_exempt
@login_required
def timestamp (request):
    if request.method == 'POST':
        id = request.POST.get('note_id')
        timestamp = cache.get('notetimestamp' + id)
        if not timestamp:
            note = get_object_or_404(Note, pk=id)
            timestamp = datetime.strftime(note.date_saved, '%d.%m.%y %I:%M')
            cache.set('notetimestamp' + str(id), HttpResponse(timestamp))
        return timestamp
    else:
        return HttpResponse(status=400)


@login_required
def tags (request):
    tags = Tag.objects.all()
    out = '['
    for t in tags:
        out += '"' + str(t) + '",'
    out = out[0:len(out)-1] + ']'

    return HttpResponse(out)