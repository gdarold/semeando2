# Generated by Django 3.1.5 on 2021-01-12 00:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doacao', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TipoPlantas',
            new_name='TipoDoacao',
        ),
        migrations.RenameModel(
            old_name='TipoDoacoes',
            new_name='TipoPlanta',
        ),
        migrations.AlterModelOptions(
            name='tipodoacao',
            options={'ordering': ('nome',), 'verbose_name': 'tipo_doacao', 'verbose_name_plural': 'tipos_doacoes'},
        ),
        migrations.AlterModelOptions(
            name='tipoplanta',
            options={'ordering': ('nome',), 'verbose_name': 'tipo_planta', 'verbose_name_plural': 'tipos_plantas'},
        ),
    ]
