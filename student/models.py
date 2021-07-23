from django.db import models

# Create your models here.
class Student(models.Model):
        first_name=models.CharField(max_length=10)
        last_name=models.CharField(max_length=10)
        age=models.PositiveIntegerField()
        date_of_birth=models.DateField()
        mentor_name=models.CharField(max_length=20)
        big_sister=models.CharField(max_length=20)
        passport_front=models.ImageField()
        passport_back=models.ImageField()
        gender=models.CharField(max_length=6)
        guardian=models.CharField(max_length=10)
        