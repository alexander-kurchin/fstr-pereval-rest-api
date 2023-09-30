from django.urls import include, path
from rest_framework import routers

from .views import PerevalAPI, PerevalViewSet


router = routers.DefaultRouter()
router.register(r'perevals', PerevalViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('submitData', PerevalAPI.as_view()),
]
