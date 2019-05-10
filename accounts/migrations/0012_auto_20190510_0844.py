# Generated by Django 2.2.1 on 2019-05-10 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20190510_0832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='org_links',
        ),
        migrations.AddField(
            model_name='user',
            name='facebook',
            field=models.CharField(blank=True, max_length=66),
        ),
        migrations.AddField(
            model_name='user',
            name='twitter',
            field=models.CharField(blank=True, max_length=66),
        ),
        migrations.AddField(
            model_name='user',
            name='website',
            field=models.CharField(blank=True, max_length=66),
        ),
        migrations.AddField(
            model_name='user',
            name='youtube',
            field=models.CharField(blank=True, max_length=66),
        ),
    ]
