from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlunoViewSet, PresencaViewSet

router = DefaultRouter()
router.register(r'alunos', AlunoViewSet)
router.register(r'presencas', PresencaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
