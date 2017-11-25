# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.db import models
import json
from collections import namedtuple

# Create your models here.


class Band(models.Model):
    name = models.CharField(max_length=200)


class Artist(models.Model):
    name = models.CharField(max_length=200)
    dateOfBirth = models.DateField()
    band = models.ForeignKey(Band, on_delete=models.CASCADE, null=True,blank=True)


class Playlist(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=500)



class Album(models.Model):
    title = models.CharField(max_length=200)
    band = models.ForeignKey(Band, on_delete=models.CASCADE, null=True,blank=True)


class Song(models.Model):
    name = models.CharField(max_length=250)
    path = models.CharField(max_length=400,null=True)
    releaseDate = models.DateField()
    genre = models.CharField(max_length=250)
    lyrics = models.CharField(max_length=2000)
    length = models.DecimalField(decimal_places=3, max_digits=6)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True,blank=True)
    playlists = models.ManyToManyField(Playlist)
    bands = models.ForeignKey(Band, on_delete=models.CASCADE, null=True,blank=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE,null=False,blank=False)




