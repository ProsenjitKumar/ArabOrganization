# Generated by Django 2.1.2 on 2018-11-05 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_auto_20181105_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_donation_date',
            field=models.DateField(default=''),
        ),
    ]
