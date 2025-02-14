from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Car, CarMark
from .serializers import CarSerializer, CarMarkSerializer

class CarListView(ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarUpDel(RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarMarkListView(ListCreateAPIView):
    queryset = CarMark.objects.all()
    serializer_class = CarMarkSerializer

class CarMarkUpDel(RetrieveUpdateDestroyAPIView):
    queryset = CarMark.objects.all()
    serializer_class = CarMarkSerializer
