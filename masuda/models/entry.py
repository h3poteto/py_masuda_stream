from django.db import models


class Entry(models.Model):
    entry_id = models.CharField(max_length=255, null=False, unique=True)
    title = models.CharField(max_length=255)
    summary = models.TextField()
    content = models.TextField()
    link = models.CharField(max_length=255, null=False, unique=True)
    hatena_bookmarkcount = models.IntegerField(null=False, default=0)
    posted_at = models.DateTimeField('posted_at', null=False, db_index=True)
    created_at = models.DateTimeField('created_at', auto_now_add=True)
    updated_at = models.DateTimeField('updated_at', auto_now=True)

    def __str__(self):
        return self.title
