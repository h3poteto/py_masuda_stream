# b.hatena.ne.jp/entry/jsonliteから取得できるブックマーク情報
from django.db import models
from .entry_detail import EntryDetail


class EntryBookmark(models.Model):
    entry_detail = models.ForeignKey(EntryDetail, on_delete=models.CASCADE)
    bookmarked_at = models.DateTimeField('posted_at', null=False, db_index=True)
    comment = models.CharField(max_length=255)
    user = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField('created_at', auto_now_add=True)
    updated_at = models.DateTimeField('updated_at', auto_now=True)

    def __str__(self):
        return self.user

    class Meta:
        unique_together = ('entry_detail', 'user')
