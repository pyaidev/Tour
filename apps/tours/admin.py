from django.contrib import admin
from .models import TravelRank,Travel,TravelTourDestination,TravelCategory,TravelTourDestinationImages
# Register your models here.


class TravelRankAdmin(admin.ModelAdmin):
    list_display = [ 'user','get_star',]
    list_filter=['user','stars',]

    def get_star(self, obj):
        return f'{obj.stars*"⭐️"}'


class TravelAdmin(TravelRankAdmin,admin.ModelAdmin):
    list_display = ('id', 'title', 'location','get_star')
    search_fields = ['title', 'location',]
    list_filter = [ 'location', 'cat', 'stars'] 
    list_display_links = ('title', 'id')
    search_help_text = 'search on here'
    filter_horizontal = ('cat', )
    date_hierarchy = 'created_at'

    def get_star(self, obj):
        return f'{obj.stars*"⭐️"}'

class TravelTourDestinationAdmin(admin.ModelAdmin):
    filter_horizontal=('images',)

# class TravelTourDestinationImagesAdmin(admin.ModelAdmin):
#     readonly_fields = ['image']

admin.site.register(TravelRank,TravelRankAdmin)
admin.site.register(Travel,TravelAdmin)
admin.site.register(TravelTourDestination,TravelTourDestinationAdmin)
admin.site.register(TravelCategory)
admin.site.register(TravelTourDestinationImages)