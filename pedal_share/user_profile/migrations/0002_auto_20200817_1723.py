# Generated by Django 3.1 on 2020-08-18 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='message',
            field=models.TextField(default='', verbose_name='Add a custom message to potential borrowers'),
        ),
    ]
