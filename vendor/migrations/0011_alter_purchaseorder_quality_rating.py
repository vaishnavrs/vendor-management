# Generated by Django 5.0.4 on 2024-05-15 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0010_alter_vendors_quality_rating_avg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='quality_rating',
            field=models.FloatField(default=0, null=True),
        ),
    ]
