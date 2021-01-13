# Generated by Django 3.1.5 on 2021-01-13 02:19

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0002_remove_endereco_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('nome', models.CharField(max_length=255, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='nome', unique=True)),
            ],
            options={
                'verbose_name': 'cidade',
                'verbose_name_plural': 'cidades',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('nome', models.CharField(max_length=255, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='nome', unique=True)),
            ],
            options={
                'verbose_name': 'estado',
                'verbose_name_plural': 'estados',
                'ordering': ('nome',),
            },
        ),
        migrations.AddField(
            model_name='endereco',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=0.0004950495049504951, editable=False, populate_from='cidade', unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='endereco',
            name='cidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='endereco', to='endereco.cidade'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='uf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='endereco', to='endereco.estado'),
        ),
    ]