# Generated by Django 4.0.3 on 2022-03-22 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoodapp', '0005_remove_posts_user_posts_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='neighbourhood',
        ),
        migrations.AddField(
            model_name='posts',
            name='Location',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
