# Generated by Django 5.1.6 on 2025-02-20 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lifttrak", "0008_remove_workout_completed_at_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="routine",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
