# Generated by Django 2.0.2 on 2018-04-15 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='qr_id',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
