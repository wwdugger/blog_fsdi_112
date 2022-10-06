from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Status(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name




class Post(models.Model):
    title = models.CharField(max_length=45)
    body = models.TextField()
    category = models.CharField(max_length=45)
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])