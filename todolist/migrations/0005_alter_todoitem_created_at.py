# Generated by Django 5.0.6 on 2024-06-21 11:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0004_alter_todoitem_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 21, 13, 49, 44, 692921)),
        ),
    ]
