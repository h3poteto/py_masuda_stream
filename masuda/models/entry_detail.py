# b.hatena.ne.jp/entry/jsonliteから取得できるブックマークに関する詳細情報
from django.db import models
from .entry import Entry


class EntryDetail(models.Model):
    entry = models.OneToOneField(Entry, on_delete=models.PROTECT)
    eid = models.CharField(max_length=255, null=False, unique=True)
    count = models.IntegerField(null=False, default=0)
    url = models.CharField(max_length=255, null=False, unique=True)
    title = models.CharField(max_length=255)
    screenshot = models.CharField(max_length=1023)
    created_at = models.DateTimeField('created_at', auto_now_add=True)
    updated_at = models.DateTimeField('updated_at', auto_now=True)

    def __str__(self):
        return self.title
