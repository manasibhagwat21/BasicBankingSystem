# Generated by Django 3.1.7 on 2021-06-23 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='funds',
            field=models.IntegerField(default=0),
        ),
    ]
