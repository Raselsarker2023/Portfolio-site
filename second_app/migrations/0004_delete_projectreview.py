# Generated by Django 5.0 on 2024-03-05 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0003_remove_comment_average_rating_projectreview'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProjectReview',
        ),
    ]
