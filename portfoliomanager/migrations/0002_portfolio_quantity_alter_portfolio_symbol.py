# Generated by Django 4.2.6 on 2023-11-13 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfoliomanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='symbol',
            field=models.CharField(default='SPY', max_length=32),
        ),
    ]
