# Generated by Django 4.1.5 on 2023-01-11 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='descricao',
            field=models.CharField(max_length=100),
        ),
    ]
