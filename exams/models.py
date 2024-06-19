from django.db import models
from django.db import models

class Exam(models.Model):
    title = models.CharField(max_length=200)
    duration = models.IntegerField(help_text="Duration in minutes")

class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    text = models.TextField()
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct_option = models.CharField(max_length=200)



# Create your models here.
