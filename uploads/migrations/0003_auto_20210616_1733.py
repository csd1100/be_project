# Generated by Django 3.2.4 on 2021-06-16 12:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('uploads', '0002_alter_uploads_file_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploads',
            name='changed_file_name',
        ),
        migrations.AlterField(
            model_name='uploads',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
