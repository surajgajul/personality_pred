from django.db import models

class Applicant(models.Model):

    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    personality=models.CharField(max_length=100)
    email=models.EmailField()
    dob=models.DateField()
    openness=models.IntegerField()
    neuroticism=models.IntegerField()
    conscientiousness=models.IntegerField()
    agreeableness=models.IntegerField()
    extraversion=models.IntegerField()
# Create your models here.
