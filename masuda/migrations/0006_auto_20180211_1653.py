# Generated by Django 2.0.1 on 2018-02-11 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('masuda', '0005_auto_20180210_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrybookmark',
            name='entry_detail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookmarks', to='masuda.EntryDetail'),
        ),
    ]
