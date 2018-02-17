# Generated by Django 2.0.1 on 2018-02-06 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('masuda', '0002_entrydetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntryBookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookmarked_at', models.DateTimeField(db_index=True, verbose_name='posted_at')),
                ('comment', models.CharField(max_length=255)),
                ('user', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
                ('entry_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='masuda.EntryDetail')),
            ],
        ),
    ]