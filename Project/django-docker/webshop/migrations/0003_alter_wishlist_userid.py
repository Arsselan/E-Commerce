# Generated by Django 4.2.7 on 2024-01-14 13:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webshop', '0002_alter_user_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
