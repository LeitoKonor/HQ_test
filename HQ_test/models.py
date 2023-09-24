from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Lesson(models.Model):
    products = models.ManyToManyField(Product)
    title = models.CharField(max_length=100)
    video_link = models.URLField()
    duration = models.IntegerField()


class LessonView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    viewed_time = models.IntegerField()
    is_viewed = models.BooleanField()
