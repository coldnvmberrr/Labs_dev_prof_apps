# Generated by Django 4.2.6 on 2024-06-17 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryPassagingCars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(verbose_name='Дата и время')),
                ('number', models.CharField(verbose_name='Номерной знак')),
                ('model', models.CharField(verbose_name='Марка автомобиля')),
            ],
            options={
                'verbose_name': 'Запись проезда автомобили',
                'verbose_name_plural': 'История проезжающих автомобилей',
            },
        ),
    ]