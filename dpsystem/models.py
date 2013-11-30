from django.db import models

class Student(models.Model):
    username = models.CharField(max_length=10)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)

    def __str__(self):
        return self.username

class Dojo(models.Model):
    dojo_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.dojo_name
