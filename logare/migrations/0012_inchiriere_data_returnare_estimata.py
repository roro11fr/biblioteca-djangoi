# Generated by Django 5.0 on 2023-12-18 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logare', '0011_inchiriere_data_inchiriere'),
    ]

    operations = [
        migrations.AddField(
            model_name='inchiriere',
            name='data_returnare_estimata',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]