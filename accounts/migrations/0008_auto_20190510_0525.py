# Generated by Django 2.2.1 on 2019-05-10 01:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20190510_0135'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_account_name', models.CharField(blank=True, max_length=100, null=True)),
                ('bank_account_no', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('bank_account_short_info', models.TextField(blank=True, null=True)),
                ('position', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='user_photo/')),
                ('permit', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(allow_unicode=True)),
                ('bank_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Bank')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='bank_account_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='bank_account_no',
        ),
        migrations.RemoveField(
            model_name='user',
            name='bank_account_short_info',
        ),
        migrations.RemoveField(
            model_name='user',
            name='bank_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='user',
            name='position',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.AddField(
            model_name='bankinfo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
