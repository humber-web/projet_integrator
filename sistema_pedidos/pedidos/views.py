from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Empresa, Pedido
from .serializers import EmpresaSerializer, PedidoSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    def perform_create(self, serializer):
        # Ao criar um pedido, garante que o estado inicial seja "PENDENTE"
        serializer.save(estado='PENDENTE')

    # Endpoint customizado para aprovação de pedidos
    def update(self, request, *args, **kwargs):
        pedido = self.get_object()
        # Exemplo de lógica de aprovação:
        if pedido.valor < 1000:
            pedido.estado = 'APROVADO'
        else:
            pedido.estado = 'AGUARDANDO_APROVACAO_MANUAL'
        pedido.save()
        serializer = self.get_serializer(pedido)
        return Response(serializer.data, status=status.HTTP_200_OK)
