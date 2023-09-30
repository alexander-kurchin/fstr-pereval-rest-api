from rest_framework import viewsets

from .models import Pereval
from .serializers import PerevalSerializer


class PerevalViewSet(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer
