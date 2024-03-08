# Generated by Django 5.0 on 2024-03-08 16:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0007_alter_comment_created_on_alter_comment_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='second_app.projectmodel'),
        ),
    ]
