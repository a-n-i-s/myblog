# Generated by Django 4.0.5 on 2022-08-15 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_remove_adminsetting_owner_usersetting_darkmode'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersetting',
            name='showcomments',
            field=models.BooleanField(default=True),
        ),
    ]
