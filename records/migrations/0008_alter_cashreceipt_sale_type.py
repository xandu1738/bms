# Generated by Django 4.1.6 on 2023-02-10 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0007_cashreceipt_sale_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashreceipt',
            name='sale_type',
            field=models.CharField(choices=[('Debit', 'Debit'), ('Credit', 'Credit')], default='Deb', max_length=8),
        ),
    ]
