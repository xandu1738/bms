# Generated by Django 4.1.6 on 2023-02-11 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0009_cashreceipt_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoicereceipt',
            name='total',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='proformareceipt',
            name='total',
            field=models.FloatField(default=0),
        ),
    ]