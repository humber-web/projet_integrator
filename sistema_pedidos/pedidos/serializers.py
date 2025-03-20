from rest_framework import serializers
from .models import Empresa, Pedido

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ['id', 'nome', 'nif', 'email']

class PedidoSerializer(serializers.ModelSerializer):
    empresa = EmpresaSerializer(read_only=True)
    empresa_id = serializers.PrimaryKeyRelatedField(
        queryset=Empresa.objects.all(), source='empresa', write_only=True
    )

    class Meta:
        model = Pedido
        fields = ['id', 'empresa', 'empresa_id', 'tipo', 'descricao', 'valor', 'data_submissao', 'estado']
        read_only_fields = ['data_submissao', 'estado']
