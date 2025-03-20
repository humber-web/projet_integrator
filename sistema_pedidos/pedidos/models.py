from django.db import models
from django.utils import timezone


class Empresa(models.Model):
    nome = models.CharField(max_length=255)
    nif = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome
    
    
    
    
class Pedido(models.Model):
    ESTADO_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('APROVADO', 'Aprovado'),
        ('REJEITADO', 'Rejeitado'),
        ('AGUARDANDO_APROVACAO_MANUAL', 'Aguardando Aprovação Manual'),
    ]

    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='pedidos')
    tipo = models.CharField(max_length=255)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_submissao = models.DateTimeField(default=timezone.now)
    estado = models.CharField(max_length=50, choices=ESTADO_CHOICES, default='PENDENTE')

    def __str__(self):
        return f"{self.empresa.nome} - {self.tipo}"