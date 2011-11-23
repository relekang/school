from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
import core

class BaseModel (models.Model):
    creator = models.ForeignKey(User, related_name='%(class)s_creator')
    saved_by = models.ForeignKey(User, related_name='%(class)s_saved_by')
    date_created = models.DateTimeField()
    date_saved = models.DateTimeField()

    def __unicode__(self):
        return self.creator.username + ' ' + str(self.id)

    class Meta:
        abstract = True
        
    def save(self, *args, **kwargs):
        #todo LOG IT
        user = core.get_current_user()
        if user.is_authenticated():
            if not self.pk: self.creator = user
            self.saved_by = user
        if not self.pk: self.date_created = datetime.now()
        self.date_saved = datetime.now()
        super(BaseModel, self).save(*args,**kwargs)