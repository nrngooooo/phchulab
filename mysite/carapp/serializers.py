from rest_framework import serializers
from .models import Car, CarMark

class CarMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMark
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    entry_photo = serializers.ImageField(use_url=True)  # Ensures full URL for images

    class Meta:
        model = Car
        fields = '__all__'
