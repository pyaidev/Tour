from django.contrib import admin
from .models import HotelCategory, HotelRank, Hotel, Room, Tour, Facility
# Register your models here.


class HotelCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ['title', ]


class FacilityAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ['title', ]
    list_display_links = ('title', 'id')
    search_help_text = 'search on here'


class HotelRankAdmin(admin.ModelAdmin):
    list_display = ['hotel', 'user','get_star',]
    list_filter=['user','stars','hotel']

    def get_star(self, obj):
        return f'{obj.stars*"⭐️"}'



class HotelAdmin(HotelRankAdmin,admin.ModelAdmin):
    list_display = ('id', 'name', 'hotel_cat', 'tour',)
    search_fields = ['name', 'tour']
    list_filter = ['hotel_cat', 'tour', 'stars'] 
    list_display_links = ('name', 'id')
    search_help_text = 'search on here'
    filter_horizontal = ('facilities', )
    date_hierarchy = 'created_at'


admin.site.register(Hotel, HotelAdmin)
admin.site.register(HotelCategory, HotelCategoryAdmin)
admin.site.register(Facility, FacilityAdmin)
admin.site.register(Room)
admin.site.register(Tour)
admin.site.register(HotelRank, HotelRankAdmin)
