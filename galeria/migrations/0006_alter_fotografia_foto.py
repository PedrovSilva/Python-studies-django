# Generated by Django 5.1.4 on 2024-12-17 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("galeria", "0005_rename_data_fatografia_fotografia_data_fotografia"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fotografia",
            name="foto",
            field=models.ImageField(blank=True, upload_to="fotos/%Y/%m/%d/"),
        ),
    ]
