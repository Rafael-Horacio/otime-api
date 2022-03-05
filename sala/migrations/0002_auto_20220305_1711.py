# Generated by Django 3.0.4 on 2022-03-05 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sala', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sala',
            name='tipos',
            field=models.ManyToManyField(blank=True, to='sala.Tipo'),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='ferramentas',
            field=models.ManyToManyField(blank=True, to='sala.Ferramenta'),
        ),
    ]