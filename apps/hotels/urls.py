from django.urls import path
from .views import hotel,hotel_filter,hotel_detail,hotel_room_detail
app_name='hotel'

urlpatterns = [
      path('',hotel,name='hotel'),
      path('<int:pk>/',hotel_detail,name='hotel-detail'),
      path('<int:pk>/<int:pk_>',hotel_room_detail,name='hotel-room-detail'),
      path('filter/',hotel_filter,name='hotel-filter'),  # type: ignore
]