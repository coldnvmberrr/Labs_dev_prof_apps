# Generated by Django 4.2.6 on 2024-06-17 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('history_passaging_cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='historypassagingcars',
            unique_together={('datetime', 'number', 'model')},
        ),
    ]