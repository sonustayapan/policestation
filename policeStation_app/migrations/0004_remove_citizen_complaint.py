# Generated by Django 3.1.7 on 2022-02-20 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('policeStation_app', '0003_auto_20220220_1314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citizen',
            name='Complaint',
        ),
    ]
