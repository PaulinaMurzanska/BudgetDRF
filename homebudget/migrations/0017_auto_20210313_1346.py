# Generated by Django 3.1.6 on 2021-03-13 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homebudget', '0016_auto_20210313_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='income',
            name='amount',
            field=models.FloatField(),
        ),
    ]
