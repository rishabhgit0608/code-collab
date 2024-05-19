from django.db import models

# Create your models here.


class Questions(models.Model):
    question_title = models.TextField(max_length=50)
    question_description = models.TextField(max_length=500)

    