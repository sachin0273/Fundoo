# Generated by Django 2.2.5 on 2019-10-13 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Note', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='note',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]
