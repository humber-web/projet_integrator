from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import EmpresaViewSet, PedidoViewSet

# Criando as rotas para os ViewSets existentes
router = DefaultRouter()
router.register(r'empresas', EmpresaViewSet)
router.register(r'pedidos', PedidoViewSet)

# Configuração do Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Minha API",
        default_version='v1',
        description="Documentação da API com Swagger",
        terms_of_service="https://www.seusite.com/termos/",
        contact=openapi.Contact(email="suporte@seusite.com"),
        license=openapi.License(name="Licença MIT"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include(router.urls)),  # Suas rotas atuais

    # URLs para a documentação do Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
