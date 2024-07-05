from django.contrib.auth.models import User
from django.db import models

class Exam(models.Model):
    title = models.CharField(max_length=200)
    duration = models.IntegerField()  # duration in minutes

    def __str__(self):
        return self.title

class ExamResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return f'{self.user.username} - {self.exam.title}'
class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    text = models.TextField()
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct_option = models.CharField(max_length=200)

class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)  # Example: BooleanField to indicate correctness

    def __str__(self):
        return f'{self.user.username} - {self.question.text}'

# Create your models here.
