# Generated by Django 3.0.4 on 2020-03-28 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20200328_2220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=15)),
                ('descricao', models.CharField(max_length=20)),
            ],
        ),
    ]
