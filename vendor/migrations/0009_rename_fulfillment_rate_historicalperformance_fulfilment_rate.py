# Generated by Django 5.0.4 on 2024-05-10 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0008_historicalperformance_quality_rating_avg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalperformance',
            old_name='fulfillment_rate',
            new_name='fulfilment_rate',
        ),
    ]
