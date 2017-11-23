from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Menu(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='name')
    parent = models.ForeignKey('self', null=True, blank=True, related_name="children")

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = 'Continent/Country/City'
