from django.db import models

class CarMark(models.Model):
    markName = models.CharField(max_length=50)
    def __str__(self):
        return self.markName
# Create your models here.
class Car(models.Model):
    car_plate = models.CharField(max_length=7, unique=True, null=True, blank=True)  # License plate number
    entry_photo = models.ImageField(upload_to='car_photos/entry/', null=True, blank=True)  # Entry photo
    markId = models.ForeignKey('CarMark', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.car_plate