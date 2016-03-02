from __future__ import unicode_literals

# django
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    owner = models.ForeignKey(User)
    title = models.CharField(
        max_length=20,
    )
    body_text = models.TextField(
        default='New manang in town!'
    )
    bg_img_url = models.URLField(blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


class Collection(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(
        unique=True,
        max_length=20,
    )
    body_text = models.TextField(
        default='New manang in town!'
    )
    bg_img_url = models.URLField(blank=True)
    posts = models.ManyToManyField(Post)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name
