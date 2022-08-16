# Generated by Django 4.0.5 on 2022-08-16 04:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_favourite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favourite',
            name='owner',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='favourites', to=settings.AUTH_USER_MODEL),
        ),
    ]
