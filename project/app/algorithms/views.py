from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.forms.models import modelformset_factory
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template.context import RequestContext
from app.algorithms.forms import AlgorithmRunningTimeForm
from app.algorithms.models import Algorithm, AlgorithmTag
from django.core.cache import cache

@login_required
def list (request, tag=False):
    if not tag:
        algorithms = cache.get('algorithms')
        if not algorithms:
            algorithms = Algorithm.objects.all().select_related('tags').order_by('name')
            cache.set('algorithms', algorithms)
    else:
        algorithms = cache.get('algorithms' + tag)
        if not algorithms:
            t = get_object_or_404(AlgorithmTag, slug=tag)
            algorithms = t.algorithms.select_related('tags').order_by('name')
            cache.set('algorithms' + tag, algorithms)
    return render_to_response('algorithms/base.html',
                             {'algorithms': algorithms},
                              context_instance=RequestContext(request))

@staff_member_required
def edit_running_time (request):
    algorithms = Algorithm.objects.all().select_related('tags').order_by('name')
    AlgorithmFormSet = modelformset_factory(Algorithm, form=AlgorithmRunningTimeForm)
    formset = AlgorithmFormSet(queryset=algorithms)
    if request.method == 'POST':
        formset = AlgorithmFormSet(request.POST, queryset=algorithms)
        if formset.is_valid():
            formset.save()
            return redirect(reverse('app.algorithms.views.list'),)

    return render_to_response('algorithms/edit_running_time.html',
                             {'formset': formset},
                              context_instance=RequestContext(request))