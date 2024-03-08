from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.

class Hotel(models.Model):
  name = models.CharField(max_length = 100)
  address = models.CharField(max_length = 200)
  pool =  models.BooleanField() # True if hotel has a swimming pool, False otherwise
  gym = models.BooleanField(default = False)    # True if hotel has a gym, False otherwise
  rating_choices = [
    (1, '1 star'),
    (2, '2 stars'),
    (3, '3 stars'),
    (4, '4 stars'),
    (5, '5 stars'),
  ]

  rating = models.IntegerField(choices=rating_choices)
 # Rating of the hotel on a scale of 1 to 5
  
  logo = models.ImageField(upload_to='hotel_images/', blank=True, null=True)
  image_1 = models.ImageField(upload_to='hotel_images/', blank=True, null=True)
  image_2 = models.ImageField(upload_to='hotel_images/', blank=True, null=True)
  image_3 = models.ImageField(upload_to='hotel_images/', blank=True, null=True)
  image_4 = models.ImageField(upload_to='hotel_images/', blank=True, null=True)

  
  def __str__(self):
    return self.name + " ("+ str(self.rating)+" stars)"
  
class RoomType(models.Model):
  type = models.CharField(max_length=5) # Type of room
  description = models.TextField()
  hotels = models.ManyToManyField(Hotel , related_name= 'roomtypes') # Related field name is by default `hotels`

  def __str__(self):
    return self.type

class Room(models.Model):
    room_number = models.IntegerField(
       validators = [
          MinLengthValidator(3),
          MaxLengthValidator(3)
       ]
    )
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, related_name='rooms')

    def __str__(self):
        return f"Room {self.room_number} ({self.room_type})"

class Reservation(models.Model):
    name = models.CharField(max_length = 100, default = None)
    phone  = models.IntegerField(default = None)
    email = models.EmailField(default = None)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()

    def __str__(self):
        return f"{self.name}'s reservation of {self.room} at {self.hotel}"
