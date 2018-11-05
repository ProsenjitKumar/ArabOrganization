# Generated by Django 2.1.2 on 2018-11-04 18:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_auto_20181105_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_donation_date',
            field=models.DateField(blank=True, default=uuid.uuid1, null=True, unique=True),
        ),
    ]
