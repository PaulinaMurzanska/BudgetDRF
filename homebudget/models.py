from django.db import models
from django.conf import settings
import datetime


class NameUserMixin(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Expenses(NameUserMixin, models.Model):
    amount = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    timestamp = models.DateTimeField()


class Income(NameUserMixin, models.Model):
    amount = models.FloatField()
    timestamp = models.DateTimeField()




