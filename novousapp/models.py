# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class fuel(models.Model):
    State = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    CompanyName = models.CharField(max_length=100)