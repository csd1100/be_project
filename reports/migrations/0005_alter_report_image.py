# Generated by Django 3.2.4 on 2021-06-16 16:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('reports', '0004_rename_report_id_report_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='image',
            field=models.ImageField(blank=True, default='report.png', upload_to='reports'),
        ),
    ]
