# Generated by Django 4.0.1 on 2022-05-11 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_alter_organization_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='logo',
            field=models.ImageField(default='default', upload_to='images/avatars/'),
            preserve_default=False,
        ),
    ]
    
