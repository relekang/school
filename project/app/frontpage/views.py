from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from app.notes.models import Course
from django.core.cache import cache

def frontpage (request):
    if request.user.is_authenticated():
        return staff_frontpage (request)
    else:
        return anonymous_frontpage(request)

def anonymous_frontpage(request):
    return render_to_response('base.html',
                              context_instance=RequestContext(request))

@login_required
def staff_frontpage(request):
    courses = cache.get('courses')
    if not courses:
        courses = Course.objects.all().select_related('notes')
        cache.set('courses', courses)
    return render_to_response('frontpage/staff.html',
                             {'courses': courses},
                              context_instance=RequestContext(request))
