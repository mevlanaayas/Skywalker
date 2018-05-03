# Generated by Django 2.0.2 on 2018-05-03 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_by', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('map_id', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'KR',
                'verbose_name_plural': 'KRs',
                'db_table': 'KRs',
            },
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_by', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('name', models.CharField(max_length=100)),
                ('coords', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Label',
                'verbose_name_plural': 'Labels',
                'db_table': 'labels',
            },
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_by', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('map_data', models.TextField()),
                ('movement_data', models.TextField()),
                ('label_data', models.TextField()),
                ('initial_data', models.TextField()),
                ('qr_id', models.IntegerField(null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Map',
                'verbose_name_plural': 'Maps',
                'db_table': 'maps',
            },
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_by', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('destination_label', models.CharField(max_length=255, verbose_name='Destination Label')),
                ('path_length', models.IntegerField(verbose_name='Path Length')),
                ('down_time', models.IntegerField(verbose_name='Down Time')),
                ('map_data', models.TextField()),
                ('movement_data', models.TextField()),
            ],
            options={
                'verbose_name': 'Stats',
                'verbose_name_plural': 'Stats',
                'db_table': 'stats',
            },
        ),
        migrations.AddField(
            model_name='label',
            name='map',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Map'),
        ),
        migrations.AlterUniqueTogether(
            name='label',
            unique_together={('name', 'map')},
        ),
    ]
