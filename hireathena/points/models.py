from __future__ import unicode_literals

from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField('date created')
    date_updated = models.DateTimeField('date updated')

    def __unicode__(self):
        return self.name

class User(models.Model):
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField('date created')
    date_updated = models.DateTimeField('date updated')

    def __unicode__(self):
        return self.name


class Points(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    points = models.IntegerField()
    reason = models.CharField(max_length=200)
    date_created = models.DateTimeField('date created')

    def __unicode__(self):
        return '%s: %s'%(self.user.name, self.points)
