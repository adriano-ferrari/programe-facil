from django.db import models


class Departamento(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class CPF(models.Model):
    numero = models.CharField(max_length=11)
    data_exp = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.numero


class Empregado(models.Model):
    nome = models.CharField(max_length=70)
    endereco = models.CharField(max_length=200, blank=False, null=False)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    idade = models.IntegerField()
    email = models.EmailField()
    cpf = models.OneToOneField(CPF, blank=True, null=True, on_delete=models.CASCADE)
    departamentos = models.ManyToManyField(Departamento, blank=True)
    foto = models.ImageField(upload_to='empregado_fotos')

    def __str__(self):
        return self.nome
    

class Telefone(models.Model):
    numero = models.CharField(max_length=15, null=False)
    descricao = models.CharField(max_length=20)
    cliente = models.ForeignKey(Empregado, on_delete=models.PROTECT)

    def __str__(self):
        return self.descricao + ' - ' + self.numero

