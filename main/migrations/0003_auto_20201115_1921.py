# Generated by Django 3.1.3 on 2020-11-15 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201115_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='Type',
            field=models.CharField(choices=[('TX', 'Text'), ('OC', 'OneChoice'), ('MC', 'ManyChoice')], default=models.CharField(max_length=200), max_length=2),
        ),
    ]
