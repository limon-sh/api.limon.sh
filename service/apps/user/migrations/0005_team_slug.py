# Generated by Django 4.0.1 on 2022-04-26 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_team_teammember_team_members_team_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='slug',
            field=models.SlugField(max_length=32, null=True),
        ),
    ]
