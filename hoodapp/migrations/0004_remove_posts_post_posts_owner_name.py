# Generated by Django 4.0.3 on 2022-03-22 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoodapp', '0003_remove_business_user_remove_posts_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='post',
        ),
        migrations.AddField(
            model_name='posts',
            name='Owner_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
