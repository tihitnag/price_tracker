# Generated by Django 5.1.2 on 2024-10-27 19:47

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="links_model",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=200)),
                ("price", models.FloatField(blank=True, max_length=200)),
                ("old_price", models.FloatField(blank=True, max_length=200)),
                ("current_price", models.FloatField(blank=True, max_length=200)),
                ("diffrence", models.FloatField(blank=True, max_length=200)),
                ("curent_date", models.DateField(auto_now=True)),
                ("url", models.URLField()),
            ],
        ),
    ]