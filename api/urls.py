from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()

router.register(r'modulo',          views.ModuloViewSet)
router.register(r'eje',             views.EjeViewSet)
router.register(r'categoria',       views.CategoriaViewSet)
router.register(r'indicador',       views.IndicadorViewSet)
router.register(r'subindicador',    views.SubindicadorViewSet)
router.register(r'evidencia',       views.EvidenciaViewSet)


urlpatterns = [
    path('', include(router.urls))
]  