# Generated by Django 4.0.5 on 2022-11-30 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0015_room_delete_roombook'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
