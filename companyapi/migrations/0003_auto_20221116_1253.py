# Generated by Django 3.1.2 on 2022-11-16 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyapi', '0002_auto_20221116_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='number_of_mines',
            field=models.PositiveIntegerField(),
        ),
    ]
