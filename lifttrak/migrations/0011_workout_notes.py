# Generated by Django 5.1.6 on 2025-02-21 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lifttrak", "0010_workout_name_alter_exercise_muscle_group"),
    ]

    operations = [
        migrations.AddField(
            model_name="workout",
            name="notes",
            field=models.TextField(blank=True, null=True),
        ),
    ]
