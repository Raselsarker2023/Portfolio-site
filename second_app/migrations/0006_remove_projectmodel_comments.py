# Generated by Django 5.0 on 2024-03-08 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0005_projectmodel_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectmodel',
            name='comments',
        ),
    ]
