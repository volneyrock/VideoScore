# Generated by Django 2.0.5 on 2018-05-22 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoScore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='date_uploaded',
            field=models.DateField(),
        ),
    ]