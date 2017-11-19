# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    date_last_modified = models.DateTimeField(blank=True, null=True)
    def publish(self):
        self.date_last_modified = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title
