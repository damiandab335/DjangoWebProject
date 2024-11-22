# Generated by Django 5.1.3 on 2024-11-21 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currencies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='CurrencyPairs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exchange_date', models.DateField()),
                ('currency_pairs', models.CharField(max_length=8)),
                ('exchange_rates', models.FloatField()),
            ],
        ),
    ]
