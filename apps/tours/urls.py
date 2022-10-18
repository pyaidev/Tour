from django.urls import path
from .views import tour,tour_single
app_name='tour'

urlpatterns = [
      path('',tour,name='tour'),
      path('<int:pk>/',tour_single,name='tour-single'),
]