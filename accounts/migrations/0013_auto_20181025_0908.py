# Generated by Django 2.1.2 on 2018-10-25 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20181025_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaluser',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10),
        ),
        migrations.AlterField(
            model_name='historicaluser',
            name='profession',
            field=models.CharField(choices=[('Student', 'Student'), ('Employer', 'Employer'), ('Unemployed', 'Unemployed'), ('Businessman', 'Businessman')], max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='profession',
            field=models.CharField(choices=[('Student', 'Student'), ('Employer', 'Employer'), ('Unemployed', 'Unemployed'), ('Businessman', 'Businessman')], max_length=20),
        ),
    ]
