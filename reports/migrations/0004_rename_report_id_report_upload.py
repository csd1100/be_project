# Generated by Django 3.2.4 on 2021-06-16 14:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('reports', '0003_alter_report_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='report_id',
            new_name='upload',
        ),
    ]
