# Generated by Django 4.1.6 on 2023-02-04 21:00

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='Employee',
        ),
        migrations.RenameModel(
            old_name='GeneralReceipts',
            new_name='GeneralReceipt',
        ),
    ]