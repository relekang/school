from datetime import datetime
from django.db import models
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.core.cache import cache
from core.tags.models import Tag
from project.core.models import BaseModel


class Course (BaseModel):
    title = models.CharField(max_length=80, verbose_name=_('title'))
    code = models.CharField(max_length=7, verbose_name=_('code'))
    def __unicode__(self):
        return self.title
    
class Note (BaseModel):
    title = models.CharField(max_length=80, verbose_name=_('title'))
    course = models.ForeignKey(Course, verbose_name=_('course'))
    content = models.TextField(verbose_name=_('content'))
    tags = models.ManyToManyField(Tag, blank=True, null=True, verbose_name=_('tags'))

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Note, self).save(*args, **kwargs)
        timestamp = datetime.strftime(self.date_saved, '%d.%m.%y %I:%M')
        cache.set('notetimestamp' + str(self.pk), HttpResponse(timestamp))