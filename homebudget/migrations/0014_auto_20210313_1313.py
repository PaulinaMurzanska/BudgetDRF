# Generated by Django 3.1.6 on 2021-03-13 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homebudget', '0013_auto_20210313_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='amount',
            field=models.PositiveIntegerField(help_text='coma as decimal separator'),
        ),
        migrations.AlterField(
            model_name='income',
            name='amount',
            field=models.PositiveIntegerField(help_text='coma as decimal separator'),
        ),
    ]
