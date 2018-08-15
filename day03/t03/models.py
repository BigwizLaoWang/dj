# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="team name"
    )
    def __str__(self):
        return self.name

class player(models.Model):
    name=models.CharField(
        max_length=30,
        verbose_name="名字"
    )
    age=models.IntegerField(
        verbose_name="age"
    )
    is_live =models.BooleanField(
        verbose_name="是否在役"
    )
    team=models.ForeignKey(
        Team,
        null=True,
        verbose_name='归属球队'
    )

    def __str__(self):
         return self.name

class IdCard(models.Model):
        num=models.CharField(
            max_length=19,
            verbose_name="身份证"
        )
        org=models.CharField(
            max_length=30,
            verbose_name=u"签发单位"
        )

class Person(models.Model):
    name=models.CharField(
        max_length=30
    )
    idcard=models.OneToOneField(
        IdCard,
        on_delete=models.PROTECT
    )

class Author(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="name"
    )
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(
        max_length=30,
        verbose_name="book name"
    )
    author= models.ManyToManyField(
        Author
    )
    def __str__(self):
        return self.title
class Humen(models.Model):
    name=models.CharField(
        max_length=30,
        verbose_name="name"
    )
    age=models.IntegerField(
        verbose_name="年纪"
    )
    height=models.FloatField(
        verbose_name="height"
    )
    class Meta:
        #是否抽象
        abstract = True

class Boy(Humen):
    salary = models.CharField(
        max_length=20
    )

class Girl(Humen):
    face_score=models.IntegerField(
        verbose_name="yanzhi"
    )