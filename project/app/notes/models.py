from django.db import models
from django.utils.translation import ugettext_lazy as _
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

    def __unicode__(self):
        return self.title