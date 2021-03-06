# Generated by Django 3.2.4 on 2021-06-16 13:06

from django.db import migrations, models

import uploads.utils


class Migration(migrations.Migration):
    dependencies = [
        ('uploads', '0003_auto_20210616_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploads',
            name='upload_id',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AlterField(
            model_name='uploads',
            name='file_name',
            field=models.FileField(upload_to=uploads.utils.path_and_rename),
        ),
    ]
