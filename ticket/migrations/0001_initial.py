# Generated by Django 4.2 on 2023-05-02 09:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Priorities',
            fields=[
                ('priority_id', models.AutoField(primary_key=True, serialize=False)),
                ('priority_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('ticket_id', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=384000)),
                ('status', models.BooleanField(default=False)),
                ('due_date', models.DateTimeField()),
                ('closed_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('issued_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('priority', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket.priorities')),
            ],
        ),
        migrations.CreateModel(
            name='Attachments',
            fields=[
                ('attachment_id', models.AutoField(primary_key=True, serialize=False)),
                ('file', models.FileField(unique=True, upload_to='')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket.tickets')),
            ],
        ),
    ]
