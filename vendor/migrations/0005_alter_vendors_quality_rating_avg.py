# Generated by Django 5.0.4 on 2024-05-07 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0004_rename_performancemodel_historicalperformance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendors',
            name='quality_rating_avg',
            field=models.FloatField(blank=True, default=0),
        ),
    ]