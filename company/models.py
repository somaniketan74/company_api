# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.postgres.fields.array import ArrayField
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200)
    profile_id = models.CharField(max_length=36, null=False, unique=True)
    logo = models.ImageField(upload_to='uploads/',null=True,blank=True)
    markets = ArrayField(models.CharField(max_length=100, blank=True, null=True),null=True)
    founded_date = models.DateField(null=True)
    website = models.CharField(max_length=255, null=True)


class Funding(models.Model):
    STAGE = (
        ('Series A', 'Series A'),
        ('Series B', 'Series B'),
        ('Series C', 'Series C'),
        ('Series D', 'Series D'),
        ('Series E', 'Series E'),
    )
    amount = models.IntegerField(null=True)
    date = models.DateField(null=True)
    stages = models.TextField(choices=STAGE)
    investors = models.TextField(null=True)
    company_id = models.ForeignKey(Company, related_name='fundings')


class Social(models.Model):
    email = models.CharField(max_length=255, null=True)
    phone_number = models.IntegerField(null=True)
    linkedin = models.TextField(max_length=255, null=True)
    twitter = models.TextField(max_length=255, null=True)
    facebook = models.TextField(max_length=255, null=True)
    company_id = models.OneToOneField(Company, related_name='social')
