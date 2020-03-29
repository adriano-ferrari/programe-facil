# Generated by Django 3.0.4 on 2020-03-28 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0009_auto_20200328_2338'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Empregado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=70)),
                ('endereco', models.CharField(max_length=200)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('idade', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('cpf', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.CPF')),
                ('departamentos', models.ManyToManyField(blank=True, null=True, to='clientes.Departamento')),
            ],
        ),
        migrations.AlterField(
            model_name='telefone',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clientes.Empregado'),
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
    ]