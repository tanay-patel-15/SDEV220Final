from django.shortcuts import render, get_object_or_404
from .models import Hotel, RoomType

def inputs(request):
  hotels = list(Hotel.objects.all())
  hotels.insert(0, None)  # Inserting None as the first element
  room_types = list(RoomType.objects.all())
  room_types.insert(0, None)
  context = {
        'hotels': hotels,
        'room_types': room_types,
    }
  

  
  return render(request, 'create_reservation.html', context)


def homepage(request):
    hotels = Hotel.objects.all()
    return render(request, 'homepage.html', {'hotels': hotels})

def hotel_detail(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    return render(request, 'hotel_detail.html', {'hotel': hotel})
