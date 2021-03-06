# Generated by Django 3.1.4 on 2020-12-22 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0020_remove_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='counter',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]
