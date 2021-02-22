# Generated by Django 3.0.11 on 2021-01-18 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webshop', '0005_auto_20210118_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='look',
            field=models.CharField(blank=True, choices=[('Kralen', 'Kralen'), ('Schakelketting', 'Schakelketting')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
