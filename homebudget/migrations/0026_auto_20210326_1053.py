# Generated by Django 3.1.6 on 2021-03-26 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homebudget', '0025_auto_20210313_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homebudget.category'),
        ),
    ]
