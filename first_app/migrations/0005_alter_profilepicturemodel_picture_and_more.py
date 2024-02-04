# Generated by Django 5.0 on 2024-01-30 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_resumemodel_google_docs_link_alter_resumemodel_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilepicturemodel',
            name='picture',
            field=models.ImageField(blank=True, help_text='Upload a PNG file', null=True, upload_to='second_app/media/uploads/'),
        ),
        migrations.AlterField(
            model_name='resumemodel',
            name='file',
            field=models.ImageField(blank=True, help_text='Upload a PNG file', null=True, upload_to='second_app/media/uploads/'),
        ),
    ]