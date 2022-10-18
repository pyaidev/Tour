from django.contrib import admin
from .models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location')

admin.site.register(Person, PersonAdmin)