# Generated by Django 4.2.13 on 2024-06-10 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("social_posts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="last_edited_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
