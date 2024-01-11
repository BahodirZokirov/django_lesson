# Generated by Django 5.0.1 on 2024-01-11 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('price', models.FloatField(max_length=10)),
                ('check_price', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
    ]