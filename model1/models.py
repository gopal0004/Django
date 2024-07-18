from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Student(models.Model):                    #Model is a class of models
    # id=models.AutoField()                       # that is added by django automatically so it is like Primary key
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    address=models.TextField(blank=True,null=True)

class Car(models.Model):
    car_name=models.CharField(max_length=100)
    speed=models.IntegerField(default=120)

    def __str__(self):
        return f"{self.id} The car name is {self.car_name} with the high speed of {self.speed}"

@receiver(post_save , sender = Car)
def call_car_api(sender , instance , **kwargs):
    print("CAR OBJECT CREATED")
    print(sender , instance , kwargs)