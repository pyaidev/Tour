from django.urls import path
from .views import service
app_name='service'

urlpatterns = [
      path('',service,name='service'),
]