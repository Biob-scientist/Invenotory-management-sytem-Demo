# Generated by Django 3.2.16 on 2023-01-17 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='avater.jpg', upload_to='profile_images'),
        ),
    ]
