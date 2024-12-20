# Generated by Django 5.1.2 on 2024-10-29 22:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("link", "0002_alter_links_model_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="links_model",
            name="current_price",
            field=models.FloatField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="links_model",
            name="diffrence",
            field=models.FloatField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="links_model",
            name="old_price",
            field=models.FloatField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="links_model",
            name="price",
            field=models.FloatField(blank=True, max_length=200, null=True),
        ),
    ]
