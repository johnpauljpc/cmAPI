# models.py

from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='videos/')
    transcript = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
