# Generated by Django 4.0.1 on 2022-05-16 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cluster', '0001_initial'),
        ('machine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='cluster',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cluster.cluster'),
        ),
    ]
