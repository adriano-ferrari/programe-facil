# Generated by Django 3.0.4 on 2020-03-29 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0012_empregado_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empregado',
            name='foto',
            field=models.ImageField(upload_to='empregado_fotos'),
        ),
    ]