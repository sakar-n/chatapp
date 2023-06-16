# Generated by Django 4.2 on 2023-05-14 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_rename_project_projectuser_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssiciateCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.companies')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.project')),
            ],
        ),
    ]