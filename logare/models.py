from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} Book'



class Inchiriere(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True, blank=True)
    data_inchiriere = models.DateTimeField(default=timezone.now)


    def data_returnare_estimata(self):
        return self.data_inchiriere + timedelta(days=14)


    def __str__(self):
        return f'{self.user.username} a inchiriat cartea {self.book.name}'
