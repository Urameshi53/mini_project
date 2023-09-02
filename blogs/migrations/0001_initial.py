# Generated by Django 4.2.2 on 2023-06-19 10:09

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
            name="Blog",
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
                ("pub_date", models.DateTimeField(verbose_name="date published")),
                ("title", models.CharField(max_length=200)),
                ("content", models.TextField()),
                ("likes", models.IntegerField()),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("GR", "General"),
                            ("LS", "LifeStyle"),
                            ("TR", "Travel"),
                            ("DS", "Design"),
                            ("CR", "Creative"),
                            ("ED", "Education"),
                        ],
                        max_length=2,
                    ),
                ),
                ("tag", models.CharField(max_length=12)),
                ("back_img", models.ImageField(upload_to="images")),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
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
                ("pub_date", models.DateTimeField(verbose_name="date published")),
                ("comment_text", models.TextField()),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "blog",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blogs.blog"
                    ),
                ),
            ],
        ),
    ]
