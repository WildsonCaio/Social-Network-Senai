# Generated by Django 5.2 on 2025-05-05 23:29

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rede_social', '0003_invite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invite',
            name='reciever',
        ),
        migrations.RemoveField(
            model_name='invite',
            name='sender',
        ),
        migrations.AlterField(
            model_name='invite',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
