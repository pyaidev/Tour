from django.shortcuts import render
from .models import About


def about(request):
    posts = About.objects.all()

    context = {
        'posts': posts
    }
    return render(request, 'about.html', context)