# Generated by Django 5.2.3 on 2025-07-02 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coach', '0003_alter_team_scouting_model_weaknesses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team_scouting_model',
            name='strengths',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='team_scouting_model',
            name='weaknesses',
            field=models.JSONField(),
        ),
    ]
