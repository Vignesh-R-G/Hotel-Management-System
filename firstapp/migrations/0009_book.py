# Generated by Django 4.0.5 on 2022-10-17 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0008_reserve'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('mno', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('indate', models.CharField(max_length=30)),
                ('outdate', models.CharField(max_length=30)),
            ],
        ),
    ]
