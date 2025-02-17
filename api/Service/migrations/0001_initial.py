# Generated by Django 4.1.5 on 2024-12-24 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_spot', models.CharField(max_length=500, verbose_name='Начало спота')),
                ('end_spot', models.CharField(max_length=500, verbose_name='Конец спота')),
                ('service_zone', models.CharField(max_length=500, verbose_name='Сервис-зона')),
            ],
            options={
                'verbose_name': 'Сходка',
                'verbose_name_plural': 'Сходки',
            },
        ),
    ]
