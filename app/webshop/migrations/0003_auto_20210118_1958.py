# Generated by Django 3.0.11 on 2021-01-18 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webshop', '0002_auto_20210118_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='jewelry_type',
            field=models.CharField(choices=[('Armband', 'Armband'), ('Ketting', 'Ketting'), ('Oorbel', 'Oorbel'), ('Hanger', 'Hanger')], max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='look',
            field=models.CharField(choices=[('Kralen', 'Kralen'), ('Schakelketting', 'Schakelketting')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.IntegerField(null=True),
        ),
    ]