from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import datetime


# Create your models here.
class Conversation(models.Model):

    name = models.CharField(max_length=256, unique=True)
    time_created = models.DateTimeField(default=datetime.datetime.now)
    likes = models.IntegerField(default=0)
    creator = models.ForeignKey(User, null=False)
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Conversation, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Comment(models.Model):

    user = models.ForeignKey(User)

    conversation = models.ForeignKey(Conversation, blank=True)
    
    text = models.TextField(max_length=1024)

    parent = models.ForeignKey('self', blank=True, null=True)

    #children = models.ManyToManyField('self')

    likes = models.IntegerField(default=0)

    def __unicode__(self):
        return (self.user + ": " + self.text)

