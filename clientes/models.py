from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=70)
    endereco = models.CharField(max_length=200, blank=False, null=False)
