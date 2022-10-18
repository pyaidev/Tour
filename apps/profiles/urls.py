from django.urls import path
from .views import profile,profile_login,profile_signup
app_name='profile'

urlpatterns = [
      path('',profile,name='profile'),
      path('login/',profile_login,name='profile_login'),
      path('signup/',profile_signup,name='profile_signup'),
      # path('logout/',profile_logout,name='profile_logout'),
]
