from django.db import models
from core.models import BaseModel
from django.utils.translation import ugettext_lazy as _

class Tag (BaseModel):
    title = models.CharField(max_length=40, verbose_name=_('title'))

    def __unicode__(self):
        return self.title