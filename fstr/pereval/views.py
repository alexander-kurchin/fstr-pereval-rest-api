from rest_framework import generics, mixins, status, viewsets
from rest_framework.response import Response

from .models import Pereval
from .serializers import PerevalSerializer


class PerevalViewSet(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer


class PerevalAPI(mixins.CreateModelMixin,
                 generics.GenericAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer

    def post(self, request, *args, **kwargs):
        serializer = PerevalSerializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            return Response({'status': status.HTTP_201_CREATED,
                             'message': 'Запись успешно создана',
                             'id': obj.id})
        if status.HTTP_400_BAD_REQUEST:
            return Response({'status': status.HTTP_400_BAD_REQUEST,
                             'message': serializer.errors})
        if status.HTTP_500_INTERNAL_SERVER_ERROR:
            return Response({'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                             'message': serializer.errors})
