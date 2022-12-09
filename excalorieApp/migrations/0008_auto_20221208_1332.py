# Generated by Django 3.2.7 on 2022-12-08 10:32

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('excalorieApp', '0007_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userfooditem',
            name='profile',
            field=models.ManyToManyField(blank=True, default=django.contrib.auth.models.User, to='excalorieApp.Profile'),
        ),
    ]
