from django.db import models

class Doador(models.Model):
    nome = models.CharField(max_length=45)
    foto_perfil = models.TextField(max_length=250, null=True)
    usuario = models.CharField(max_length=45, unique=True)

class Cartao(models.Model):
    nome = models.CharField(max_length=25)
    numero = models.IntegerField()
    validade = models.DateTimeField()
    doador = models.ForeignKey(Doador, on_delete=models.CASCADE)

class CriadorCampanha(models.Model):
    nome = models.CharField(max_length=100)
    usuario = models.CharField(max_length=45, unique=True)
    foto_perfil = models.TextField(max_length=250, null=True)

class Campanha(models.Model):
    descricao = models.TextField()
    titulo = models.CharField(max_length=60)
    meta = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.TextField(max_length=250, null=True)
    video = models.TextField(max_length=250, null=True)
    criador = models.ForeignKey(CriadorCampanha, on_delete=models.CASCADE)

class Doacao(models.Model):
    data = models.DateTimeField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    forma_pagamento = models.CharField(max_length=60)
    doador = models.ForeignKey(Doador, on_delete=models.CASCADE)
    campanha = models.ForeignKey(Campanha, on_delete=models.CASCADE)
