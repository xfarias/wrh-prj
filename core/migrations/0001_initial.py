# Generated by Django 2.2 on 2019-04-17 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome da Empresa')),
                ('endereco', models.CharField(max_length=250, verbose_name='Endereço')),
                ('cidade', models.CharField(max_length=80, verbose_name='Cidade')),
                ('estado', models.CharField(max_length=100, verbose_name='estado')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Requisitos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requisitos_especificos', models.TextField(verbose_name='Requisitos Específicos')),
                ('requisitos_gerais', models.TextField(verbose_name='Requisitos Gerais')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Empresa')),
            ],
            options={
                'verbose_name': 'Requisito',
                'verbose_name_plural': 'Requisitos',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('descricao', models.TextField()),
                ('salario', models.FloatField()),
                ('tipo_contrato', models.CharField(choices=[('PJ', 'Pessoa Juridica'), ('CLT', 'Consolidação das Leis do Trabalho')], max_length=50)),
                ('status', models.BooleanField(default=1)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Empresa')),
                ('requisitos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Requisitos')),
            ],
        ),
    ]
