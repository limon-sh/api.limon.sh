# Generated by Django 4.0.1 on 2022-05-12 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='logo',
            field=models.ImageField(null=True, upload_to='images/logo/'),
        ),
    ]
