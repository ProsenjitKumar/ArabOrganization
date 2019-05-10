# Generated by Django 2.2.1 on 2019-05-10 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20190510_0625'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrgLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=66)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='org_links',
        ),
        migrations.AddField(
            model_name='user',
            name='org_links',
            field=models.ManyToManyField(blank=True, to='accounts.OrgLinks'),
        ),
    ]
