from django.db import models

class Chef(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Receita(models.Model):
    nome = models.CharField(max_length=30)
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
    receita = models.TextField()

    def __str__(self):
        return self.nome