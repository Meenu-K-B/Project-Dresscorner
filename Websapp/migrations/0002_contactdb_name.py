# Generated by Django 5.1.2 on 2024-10-29 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Websapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactdb',
            name='Name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
