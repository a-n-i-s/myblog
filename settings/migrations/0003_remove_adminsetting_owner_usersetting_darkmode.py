# Generated by Django 4.0.5 on 2022-08-15 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminsetting',
            name='owner',
        ),
        migrations.AddField(
            model_name='usersetting',
            name='darkmode',
            field=models.BooleanField(default=False),
        ),
    ]
