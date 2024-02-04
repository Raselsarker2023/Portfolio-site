# Generated by Django 5.0 on 2024-01-30 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_alter_resumemodel_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='resumemodel',
            name='google_docs_link',
            field=models.URLField(blank=True, help_text='Provide a Google Docs link', null=True),
        ),
        migrations.AlterField(
            model_name='resumemodel',
            name='file',
            field=models.FileField(blank=True, help_text='Upload a PNG file', null=True, upload_to='static/resume.png'),
        ),
    ]