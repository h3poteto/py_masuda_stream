from django.db import models
from .entry import Entry


class Anond(models.Model):
    entry = models.OneToOneField(Entry, on_delete=models.PROTECT)
    content_html = models.TextField()
    created_at = models.DateTimeField('created_at', auto_now_add=True)
    updated_at = models.DateTimeField('updated_at', auto_now=True)

    def __str__(self):
        return str(self.id)
