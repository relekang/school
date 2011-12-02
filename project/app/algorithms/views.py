from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from app.algorithms.models import Algorithm, AlgorithmTag
from django.core.cache import cache

@login_required
def list (request, tag=False):
    if not tag:
        algorithms = cache.get('algorithms')
        if not algorithms:
            algorithms = Algorithm.objects.all().select_related('tags')
            cache.set('algorithms', algorithms)
    else:
        algorithms = cache.get('algorithms' + tag)
        if not algorithms:
            t = get_object_or_404(AlgorithmTag, slug=tag)
            algorithms = t.algorithms.select_related('tags')
            cache.set('algorithms' + tag, algorithms)
    return render_to_response('algorithms/base.html',
                             {'algorithms': algorithms},
                              context_instance=RequestContext(request))