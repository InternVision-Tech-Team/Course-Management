# Generated by Django 5.2 on 2025-06-17 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_icon', models.CharField(max_length=100)),
                ('service_title', models.CharField(max_length=100)),
                ('service_des', models.TextField()),
            ],
        ),
    ]
