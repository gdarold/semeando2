# Generated by Django 3.1.5 on 2021-01-08 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cpf',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='user',
            name='telefone',
            field=models.CharField(max_length=20),
        ),
    ]
