from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    age = models.IntegerField()
    campus = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-updated']
class App(models.Model):
    name = models.CharField(max_length=50)
    auther = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
