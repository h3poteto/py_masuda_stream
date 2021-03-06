# Generated by Django 2.0.1 on 2018-02-05 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_id', models.CharField(max_length=255, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('summary', models.TextField()),
                ('content', models.TextField()),
                ('link', models.CharField(max_length=255, unique=True)),
                ('hatena_bookmarkcount', models.IntegerField(default=0)),
                ('posted_at', models.DateTimeField(db_index=True, verbose_name='posted_at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
            ],
        ),
    ]
