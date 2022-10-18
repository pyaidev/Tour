from django.shortcuts import render
from .models import Travel
from apps.profiles.models import MyTravel
# Create your views here.

def tour(request):
      travels=Travel.objects.all()
      locations={}
      for i,k in enumerate(travels):
            if k.location not in locations.values():
                  locations[i]=k.location
      context={
            'travels':travels,
            'locations':locations,
      }
      return render(request, 'tours.html',context)


def tour_single(request,pk=None):
      
      travel=Travel.objects.get(id=pk)
      if request.method == 'POST':
            
            get_ratel=MyTravel(profile=request.user.profile,travel_id=pk)
            get_ratel.save()

      context={
            'travel':travel,
      }
      return render(request,'tour-place.html',context)