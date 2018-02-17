# Generated by Django 2.0.1 on 2018-02-06 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('masuda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntryDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=255, unique=True)),
                ('count', models.IntegerField(default=0)),
                ('url', models.CharField(max_length=255, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('screenshot', models.CharField(max_length=1023)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
                ('entry', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='masuda.Entry')),
            ],
        ),
    ]