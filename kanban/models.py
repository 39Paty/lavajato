from django.db import models

class Vehicle(models.Model):
    SERVICE_CHOICES = [
        ('simples', 'Lavagem Simples'),
        ('completa', 'Lavagem Completa'),
        ('higienizacao', 'Higienização'),
    ]

    STAGE_CHOICES = [
        ('aguardando', 'Aguardando Atendimento'),
        ('externa', 'Lavagem Externa'),
        ('interna', 'Limpeza Interna'),
        ('finalizacao', 'Finalização'),
        ('pronto', 'Pronto para Entrega'),
    ]

    cliente = models.CharField(max_length=100)
    placa = models.CharField(max_length=10)
    servico = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    observacoes = models.TextField(blank=True)
    chegada = models.DateTimeField(auto_now_add=True)
    etapa = models.CharField(max_length=20, choices=STAGE_CHOICES, default='aguardando')

    def __str__(self):
        return f"{self.cliente} - {self.placa}"

