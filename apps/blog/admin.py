from django.contrib import admin
from .models import Blog, Categories

admin.site.register(Blog),
admin.site.register(Categories)