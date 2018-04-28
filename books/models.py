# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    image_url = models.ImageField(upload_to='pic_folder/')


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal('0.00')
    )


class ReadStatus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    READ_STATUS_CHOICES = (
        (1, 'Want to read'),
        (2, 'Read')
    )

    status = models.IntegerField(
        choices=READ_STATUS_CHOICES,
        default=0
    )
