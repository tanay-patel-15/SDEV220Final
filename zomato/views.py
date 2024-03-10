from django.shortcuts import render, get_object_or_404, redirect
from .models import Hotel, RoomType, Reservation

def inputs(request):
   
    # Handle the case when the form is not submitted or incomplete
    hotels = Hotel.objects.all()
    room_types = RoomType.objects.all()
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

def reservation_success(request):
    name = request.GET.get('name')
    phone = request.GET.get('phone')
    email = request.GET.get('email')
    hotel_id = request.GET.get('hotel')
    room_type_id = request.GET.get('room')
    check_in_date = request.GET.get('check_in_date')
    check_out_date = request.GET.get('check_out_date')

    
    # Get the selected hotel and room type objects
    hotel = Hotel.objects.get(pk=hotel_id)
    room_type = RoomType.objects.get(pk=room_type_id)

    # Create a reservation object
    reservation = Reservation(
        name=name,
        phone=phone,
        email=email,
        hotel=hotel,
        room=room_type,
        check_in_date=check_in_date,
        check_out_date=check_out_date
    )
    reservation.save()

    res = get_object_or_404(Reservation, name=name)
    res_id = res.id


    return render(request, 'reservation_success.html', {'reservation': reservation, 'res_id': res_id})

