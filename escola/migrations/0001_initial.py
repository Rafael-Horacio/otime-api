# Generated by Django 3.0.3 on 2020-10-19 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sala', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Escola',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('periodo_letivo', models.CharField(max_length=100)),
                ('aulas_por_turno', models.IntegerField()),
                ('dia_por_semana', models.IntegerField()),
                ('salas', models.ManyToManyField(to='sala.Sala')),
            ],
            options={
                'verbose_name_plural': 'Escolas',
                'db_table': 'escola',
            },
        ),
    ]