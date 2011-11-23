from django.db import models
from project.core.models import BaseModel

class Note (BaseModel):
    title = models.CharField(max_length=80)
    content = models.TextField()

    def __unicode__(self):
        return self.title