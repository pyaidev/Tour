from django.shortcuts import render,redirect
from .models import Car,Rent
from .models import Services

def service(request):
      service = Services.objects.all()
      context = {
            'service': service
      }
      print(request.POST.get('where'))
      return render(request, 'services.html', context)