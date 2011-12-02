from django.db import models
from core.models import BaseModel
from django.utils.translation import ugettext_lazy as _
from django.core.cache import cache

class AlgorithmTag (BaseModel):
    title = models.CharField(max_length=50)
    slug = models.CharField(max_length=40)

    def __unicode__(self):
        return self.title

    
class Algorithm (BaseModel):
    name = models.CharField(max_length=60, verbose_name=_('name'))
    description = models.TextField(blank=True,verbose_name=_('description'))
    pros = models.TextField(blank=True,verbose_name=_('pros'))
    cons = models.TextField(blank=True,verbose_name=_('cons'))
    time_best_case = models.CharField(max_length=30, blank=True, verbose_name=_('best case'))
    time_worst_case = models.CharField(max_length=30, blank=True, verbose_name=_('worst case'))
    tags = models.ManyToManyField(AlgorithmTag, blank=True, null=True,related_name='algorithms',verbose_name=_('tags'))

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Algorithm, self).save(*args, **kwargs)
        cache.set('algorithms', list(Algorithm.objects.all().select_related('tags').order_by('name')))
        for t in self.tags.all():
            cache.set('algorithms' + t.slug, list(t.algorithms.select_related('tags').order_by('name')))
