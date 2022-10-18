from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from apps.profiles.forms import RegisterForm
from .models import Profile,MyHotel,MyTravel

# Create your views here.
def profile(request):
      hotels=MyHotel.objects.filter(profile_id=request.user.profile.id)
      travels=MyTravel.objects.filter(profile_id=request.user.profile.id)
      hid=request.GET.get('hotel')
      tid=request.GET.get('travel')
      if hid:
           MyHotel.objects.get(id=hid).delete()
           return redirect('/profile/')
      
      if tid:
           MyTravel.objects.get(id=tid).delete()
           return redirect('/profile/')
      
      if request.method == 'POST':
        logout(request)
        return redirect('/')


      context={
            'hotels':hotels,
            'travels':travels
      }
      return render(request, 'profile/index.html',context)


def profile_login(request):
      if request.user.is_authenticated:
            return redirect('/profile/logout')
      form=AuthenticationForm(request)
      if request.method == 'POST':
            form=AuthenticationForm(request,data=request.POST)
            if form.is_valid():
                  user=form.get_user()
                  login(request,user)
                  return redirect('/')
      return render(request, 'accounts/login.html',{'form':form})


def profile_signup(request):
      if request.user.is_authenticated:
            return redirect('/profile/logout')
      form=RegisterForm(request.POST or None)
      if request.method == 'POST':
            if form.is_valid():
                  form.save()
                  username=form.cleaned_data.get('username')
                  user=User.objects.get(username=username)
                  login(request, user)
                  Profile.objects.create(
                        account=user,
                  )
                  return redirect('/')
      context={'form': form}
      return render(request, 'accounts/register.html',context)