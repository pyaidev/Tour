from django.contrib import admin
from .models import Rent, Car, Cat, Services

admin.site.register(Cat)
admin.site.register(Car)
admin.site.register(Rent)
admin.site.register(Services)