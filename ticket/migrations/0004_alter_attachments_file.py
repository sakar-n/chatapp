# Generated by Django 4.2 on 2023-05-17 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_alter_attachments_file_alter_priorities_company_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachments',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
    ]
