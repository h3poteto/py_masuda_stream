# Generated by Django 2.0.1 on 2018-02-10 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('masuda', '0003_entrybookmark'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anond',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_html', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
                ('entry', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='masuda.Entry')),
            ],
        ),
    ]