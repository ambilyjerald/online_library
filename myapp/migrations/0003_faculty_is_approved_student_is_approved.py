# Generated by Django 5.0.6 on 2024-06-28 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_add_book_feedback"),
    ]

    operations = [
        migrations.AddField(
            model_name="faculty",
            name="is_approved",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="student",
            name="is_approved",
            field=models.BooleanField(default=False),
        ),
    ]