# Generated by Django 4.0.3 on 2022-03-22 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hoodapp', '0006_remove_posts_neighbourhood_posts_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='title',
        ),
    ]
