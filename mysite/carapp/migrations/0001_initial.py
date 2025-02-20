# Generated by Django 5.0.11 on 2025-01-31 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_plate', models.CharField(blank=True, max_length=7, null=True, unique=True)),
                ('entry_photo', models.ImageField(blank=True, null=True, upload_to='car_photos/entry/')),
            ],
        ),
    ]
