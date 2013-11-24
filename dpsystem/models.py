from django.db import models

class Student(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    students_dojo = models.ForeignKey('Dojo')

class Dojo(models.Model):
    dojo_name = models.CharField(max_length=50)
    dojo_admin = models.ForeignKey('Instructors')

class Instructors(models.Model):
    uname = models.CharField(max_length=15)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
