# Generated by Django 4.2 on 2023-05-24 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0009_messagemodel_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachments',
            name='message',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ticket.messagemodel'),
            preserve_default=False,
        ),
    ]
