# Generated by Django 2.0.1 on 2018-02-10 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('masuda', '0004_anond'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='entrybookmark',
            unique_together={('entry_detail', 'user')},
        ),
    ]