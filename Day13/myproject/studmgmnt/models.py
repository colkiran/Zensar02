from django.db import models

# Create your models here.
class Stud(models.Model):
    stud_name = models.CharField(max_length=50)
    stud_dob = models.CharField(max_length=20)
    stud_class = models.CharField(max_length=30)

