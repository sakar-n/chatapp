# Generated by Django 4.2 on 2023-05-19 06:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0008_assiciatecompany_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForeignUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('associate_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.assiciatecompany')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
