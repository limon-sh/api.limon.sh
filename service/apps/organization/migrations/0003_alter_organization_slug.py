# Generated by Django 4.0.1 on 2022-04-26 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_organization_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='slug',
            field=models.SlugField(max_length=32, null=True),
        ),
    ]