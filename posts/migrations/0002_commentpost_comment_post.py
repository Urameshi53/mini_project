# Generated by Django 4.2.2 on 2023-07-14 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="commentpost",
            name="comment_post",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="posts.commentpost",
            ),
        ),
    ]
