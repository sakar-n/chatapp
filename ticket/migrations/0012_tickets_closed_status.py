# Generated by Django 4.2 on 2023-05-24 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0011_remove_attachments_message_messageattachments'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='closed_status',
            field=models.BooleanField(default=False),
        ),
    ]
