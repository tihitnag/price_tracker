# Generated by Django 5.1.2 on 2024-10-31 14:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("link", "0003_alter_links_model_current_price_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="links_model",
            name="name",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
