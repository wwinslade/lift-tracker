# Generated by Django 5.1.6 on 2025-02-11 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lifttrak", "0004_alter_customexercise_muscles_targeted_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="workouttemplate",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
