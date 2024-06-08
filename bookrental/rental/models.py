from django.db import models
from django.utils import timezone
from datetime import timedelta

class Student(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    page_count = models.IntegerField()

    def __str__(self):
        return self.title
