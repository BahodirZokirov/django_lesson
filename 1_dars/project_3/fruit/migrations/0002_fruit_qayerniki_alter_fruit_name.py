# Generated by Django 5.0.1 on 2024-01-11 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fruit',
            name='qayerniki',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='fruit',
            name='name',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
