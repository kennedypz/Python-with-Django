from django.db import models

# Create your models here.

class Proprietario(models.Model):
    SEXO_CHOICES = {
        ("feminino", "Feminino"),
        ("masculino", "Masculino"),
    }
    nome = models.CharField(max_length=50, null=False)
    data_nascimento = models.DateTimeField(null=False, verbose_name="Data de Nascimento")
    cpf = models.CharField(null=False, max_length=20)
    sexo = models.CharField(max_length=20, null=False, choices=SEXO_CHOICES)
    profissao = models.CharField(max_length=20)
    telefone = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.nome


class Acessorio(models.Model):
    ESTADO_CHOICES = {
        ("Ótimo", "ótimo"),
        ("Bom", "bom"),
        ("Ruim", "ruim")
    }
    descricao = models.CharField(max_length=50, null=False)
    estado = models.CharField(max_length=20, null=False, choices=ESTADO_CHOICES)

    def __str__(self):
        return self.descricao


class Veiculo(models.Model):
    CORES_CHOICES = {
        ("Amarelo", "amarelo"),
        ("Azul", "azul"),
        ("Branco", "branco"),
        ("Prata", "prata"),
        ("Preto", "preto"),
        ("Vermelho", "vermelho")
    }

    TIPO_CHOICES = {
        ("Carro", "carro"),
        ("Moto", "moto")
    }

    modelo = models.CharField(max_length=50, null=False)
    marca = models.CharField(max_length=20, null=False)
    placa = models.CharField(max_length=8, null=False)
    cor = models.CharField(max_length=20, null=False, choices=CORES_CHOICES)
    ano = models.CharField(max_length=4, null=False)
    preco = models.FloatField(null=False)
    foto_capa = models.ImageField(upload_to='images')
    tipo = models.CharField(max_length=10, null=False, choices=TIPO_CHOICES)
    proprietario = models.ForeignKey(Proprietario, on_delete=models.PROTECT)
    acessorios = models.ForeignKey(Acessorio, on_delete=models.PROTECT)

    def __str__(self):
        return self.modelo
