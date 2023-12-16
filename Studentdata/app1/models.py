from django.db import models

# Create your models here.

class Studentrecord(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    age = models.IntegerField()
    grade = models.FloatField()

