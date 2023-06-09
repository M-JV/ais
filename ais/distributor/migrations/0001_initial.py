# Generated by Django 4.2.2 on 2023-06-20 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Distributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distributorName', models.CharField(max_length=20)),
                ('distributorEmail', models.EmailField(max_length=50)),
                ('distributorContact', models.CharField(max_length=11)),
                ('distributorPassword', models.CharField(max_length=20)),
                ('distributorToken', models.CharField(default='0000', max_length=4)),
            ],
            options={
                'db_table': 'Distributor Info',
            },
        ),
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requestName', models.CharField(max_length=20)),
                ('requestPrice', models.FloatField()),
                ('distributorId', models.IntegerField()),
                ('requestDetails', models.TextField()),
            ],
            options={
                'db_table': 'Requests Info',
            },
        ),
        migrations.CreateModel(
            name='TemporaryD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distributorName', models.CharField(max_length=20)),
                ('distributorPassword', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Distributor Temporary Data',
            },
        ),
    ]
