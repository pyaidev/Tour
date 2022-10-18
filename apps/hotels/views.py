from django.shortcuts import render, redirect
from .models import Hotel, HotelCategory, Room, Tour
from django.http import JsonResponse
from apps.profiles.models import MyHotel
from django.core.paginator import Paginator
from datetime import datetime, date
from django.db.models import Q


# Create your views here.


def hotel(request):
    hotels = Hotel.objects.all()
    stars_ = request.POST.getlist('stars')  # requestdan kelgan stars
    hotel_cats_ = request.POST.getlist('cats')
    locations = request.POST.getlist('locations')  # request
    # not_filter_hotels=Hotel.objects.all()
    _stars = [int(i) for i in stars_]

    if _stars:
        hotels = hotels.filter(stars__in=_stars)

    if hotel_cats_:
        hotel_cat = Hotel.objects.none()
        for i in hotel_cats_:
            hotel_cat = hotel_cat.union(Hotel.objects.filter(hotel_cat__title=i))
        hotels = hotels.intersection(hotel_cat)

    if locations:
        hotel_locations = Hotel.objects.none()
        for i in locations:
            hotel_locations = hotel_locations.union(Hotel.objects.filter(tour__title=i))
        hotels = hotels.intersection(hotel_locations)

        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        room = rooms.filter(~Q(check_out__range=[check_in, check_out]), ~Q(check_in__range=[check_in, check_out]))

    context = {
        'hotels': hotels,
        'cats': HotelCategory.objects.all(),
        'tours': Tour.objects.all(),
        'stars': stars_,
        'hotel_cats_': hotel_cats_,
        'locations': locations,

    }
    return render(request, 'hotel.html', context)


def hotel_detail(request, pk):
    hotel = Hotel.objects.get(id=pk)
    rooms = hotel.rooms.all()
    # rooms=rooms.filter(datetime.date(2009,8,22))

    cat = request.GET.get('cat')
    if request.method == 'POST':
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        room = rooms.filter(~Q(check_out__range=[check_in, check_out]), ~Q(check_in__range=[check_in, check_out]))

        rooms = room

    if cat != None:
        rooms = rooms.filter(cat__exact=cat)
    p = Paginator(rooms, 12)
    page = request.GET.get('page')
    posts_ = p.get_page(page)

    return render(request, 'hotels.html', {'hotel': hotel, 'rooms': posts_})


def hotel_filter(request):
    hotels = Hotel.objects.all()

    sid = request.POST.get('_cid')

    if sid:
        hotels = Hotel.objects.filter(stars=int(sid))
    context = {
        'hotels': hotels, }
    return render(request, 'hotel.html', context)


def hotel_room_detail(request, pk, pk_):
    if request.method == 'POST':
        buy_room = MyHotel(profile=request.user.profile, hotels_id=pk, rooms_id=pk_)
        if buy_room not in MyHotel.objects.filter(profile_id=request.user.profile.id):
            buy_room.save()
            get_room = Room.objects.get(id=pk_)
            get_room.empty = True
            get_room.save()
            return redirect(f'/hotel/{pk}/')

    room = Room.objects.get(id=pk_)

    return render(request, 'room.html', {'room': room})
