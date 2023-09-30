from django.urls import include, path
from .views import PerevalViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'perevals', PerevalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
