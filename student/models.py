from django.db import models

# Create your models here.
class Student(models.Model):
        first_name=models.CharField(max_length=10)
        last_name=models.CharField(max_length=10)
        age=models.PositiveIntegerField()
        date_of_birth=models.DateField()