# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=32,default='title')
    content = models.TextField(null=True)

    def __unicode__(self):
        return self.title