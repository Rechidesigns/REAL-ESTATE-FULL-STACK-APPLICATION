# Generated by Django 4.1.3 on 2022-11-27 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestateapp', '0003_rename_numbers_of_bathrooms_listing_num_bathrooms_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='image',
            field=models.ImageField(default=False, upload_to=''),
        ),
    ]
