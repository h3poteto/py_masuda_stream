from django.db import models

class Entry(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    url = models.CharField(max_length=255)
    posted_at = models.DateTimeField('posted_at')
    created_at = models.DateTimeField('created_at', auto_now_add=True)
    updated_at = models.DateTimeField('updated_at', auto_now=True)

    def __str__(self):
        return self.title
