# Generated by Django 4.2.2 on 2023-07-18 15:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("blogs", "0005_alter_blog_pub_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="pub_date",
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
