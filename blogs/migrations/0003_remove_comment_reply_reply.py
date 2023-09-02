# Generated by Django 4.2.2 on 2023-07-14 22:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blogs", "0002_comment_reply"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="reply",
        ),
        migrations.CreateModel(
            name="Reply",
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
                ("content", models.CharField(max_length=240)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "comment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blogs.comment"
                    ),
                ),
            ],
        ),
    ]