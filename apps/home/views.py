import json
from django.shortcuts import render
from apps.hotels.models import Hotel
from apps.blog.models import Blog
from apps.tours.models import Travel
from .models import Person

def divide_chunks(l, n):#kkli

    for i in range(0, len(l), n):
        yield l[i:i + n]


# Create your views here.
def home(request):
      tours=Travel.objects.all()
      persons = Person.objects.all()
      destations=tours[:8]
      countr=False
      if destations.count()>4:
            countr=True

      a=[i.location for i in tours]
      locations=dict()
      for i,k in enumerate(divide_chunks(a, n=5)):
            locations[i]=k
      
      if request.GET:
            print(request.GET.get('subscribe'))  #contactga save 
      context={
            'destations':Travel.objects.all()[:8],
            'blogs':Blog.objects.all().order_by('-id')[:4],
            'hotels':Hotel.objects.all(),
            'hotel_4':countr,
            'locations':locations,
            'persons': persons
      }
      
      return render(request, 'index.html',context)
