from rest_framework import serializers
from .models import Car, CarMark

class CarMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMark
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    entry_photo = serializers.ImageField(use_url=True)
    markId = CarMarkSerializer()  # Expecting an ID, not an object
    class Meta:
        model = Car
        fields = '__all__'
    def create(self, validated_data):
        mark_data = validated_data.pop('markId', None)
        if mark_data:
            validated_data['markId'] = mark_data
        return Car.objects.create(**validated_data)



