# Generated by Django 4.0.3 on 2022-03-21 08:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NeighbourHood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Location', models.CharField(max_length=255)),
                ('Occupants', models.IntegerField()),
                ('Admin', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_name', models.CharField(max_length=255)),
                ('neighbourHood', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='hoodapp.neighbourhood')),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Business_name', models.CharField(max_length=255)),
                ('Business_email', models.EmailField(max_length=254)),
                ('User', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='hoodapp.user')),
            ],
        ),
    ]
