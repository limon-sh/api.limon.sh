# Generated by Django 4.0.4 on 2022-05-26 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0006_alter_organization_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='libs.storages.LocalMediaStorage'),
        ),
    ]
