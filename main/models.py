from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.core.files import File
import requests, os, urllib
from urlparse import urlparse 
import urllib2
from django.core.files.base import ContentFile

def get_remote_image(self):
    if self.icon_url and not self.icon:
        result = urllib.urlretrieve(self.icon_url)
        self.icon.save(
                os.path.basename(self.icon_url),
                File(open(result[0]))
                )
        self.save()

class Component(models.Model):
    name = models.CharField(max_length=50)
    stars = models.IntegerField(default=0)
    downloads = models.BigIntegerField(default=0)
    created_time = models.DateTimeField(editable=False)
    modified_time = models.DateTimeField()
    tags = models.ManyToManyField('Tag')
    icon_url = models.URLField(null=True, blank=True)
    icon = models.ImageField(null=True, upload_to='icons/')
    github_url = models.URLField(null=True)
    short_description = models.TextField(null=True)
    url_name = models.SlugField(null=True, unique=True)
    commits = models.IntegerField(default=0)
    forks = models.IntegerField(default=0)
    wwatchers = models.IntegerField(default=0)
    no_of_contributors = models.IntegerField(default=0)
    version = models.CharField(max_length=20, null=True)
    no_of_releases = models.IntegerField(default=0)
    open_issues = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_time = timezone.now()
        self.modified_time = timezone.now()
        if not self.icon:
            get_remote_image(self)
        if not self.url_name:
            self.url_name = (str(self.name).replace(' ', '-')).lower()
        return super(Component, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

class Contributor(models.Model):
    username = models.CharField(max_length=100)
    avatar_url = models.URLField()
    components = models.ManyToManyField(Component, through="Contribution")

    def __unicode__(self):
        return self.username

class Contribution(models.Model):
    contributor = models.ForeignKey(Contributor, on_delete=models.SET_NULL, null=True)
    component = models.ForeignKey(Component, on_delete=models.SET_NULL, null=True)
    contributions = models.IntegerField(default=0)