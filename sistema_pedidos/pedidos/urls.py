from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmpresaViewSet, PedidoViewSet

router = DefaultRouter()
router.register(r'empresas', EmpresaViewSet)
router.register(r'pedidos', PedidoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
