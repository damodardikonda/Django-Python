# Generated by Django 3.1.4 on 2020-12-22 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0019_workersrequests_recruiter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
    ]
