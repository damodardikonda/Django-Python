# Generated by Django 3.1.4 on 2020-12-21 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0017_auto_20201220_0619'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruitersrequests',
            name='recruiter',
            field=models.IntegerField(default=14),
            preserve_default=False,
        ),
    ]
