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
class Rental(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rental_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def rental_duration(self):
        if self.return_date:
            return (self.return_date - self.rental_date).days
        return (timezone.now().date() - self.rental_date).days

    def is_overdue(self):
        return self.rental_duration() > 30

    def overdue_fee(self):
        if not self.is_overdue():
            return 0
        overdue_days = self.rental_duration() - 30
        monthly_fee = self.book.page_count / 100.0
        overdue_months = (overdue_days // 30) + (1 if overdue_days % 30 > 0 else 0)
        return monthly_fee * overdue_months