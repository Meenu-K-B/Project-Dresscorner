# Generated by Django 5.1.2 on 2024-11-17 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Websapp', '0004_cartdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Email', models.CharField(blank=True, max_length=100, null=True)),
                ('Place', models.CharField(blank=True, max_length=100, null=True)),
                ('Address', models.CharField(blank=True, max_length=100, null=True)),
                ('Mobile', models.IntegerField(blank=True, null=True)),
                ('State', models.CharField(blank=True, max_length=100, null=True)),
                ('Pin', models.IntegerField(blank=True, null=True)),
                ('TotalPrice', models.IntegerField(blank=True, null=True)),
                ('Messages', models.TextField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]
