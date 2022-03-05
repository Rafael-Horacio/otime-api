# Generated by Django 3.0.4 on 2022-03-05 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('abreviatura', models.CharField(blank=True, max_length=25, null=True)),
                ('coordenador', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Professores',
                'db_table': 'Professor',
            },
        ),
    ]
