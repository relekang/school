from django.shortcuts import render_to_response
from django.template.context import RequestContext
from app.algorithms.models import Algorithm

def list (request, tag=False):
    algorithms = Algorithm.objects.all()
    return render_to_response('algorithms/base.html',
                             {'algorithms': algorithms},
                              context_instance=RequestContext(request))