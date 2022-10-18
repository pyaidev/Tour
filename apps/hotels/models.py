from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.signals import post_save, pre_save
# Create your models here.


class HotelCategory(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Room(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='hotels',null=True)
    price = models.IntegerField()
    check_in=models.DateField(null=True)
    check_out=models.DateField(null=True)
    cat=models.CharField(max_length=255 ,null=True)
    empty=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title


class Tour(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Facility(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


def path_to_hotel_image(instance, filename):
    category = instance.hotel_cat.title
    tour = instance.tour
    name = instance.name
    return 'hotels/{0}/{1}/{2}images/{3}'.format(tour, category, name, filename)


class Hotel(models.Model):
    name = models.CharField(max_length=255)
    hotel_cat = models.ForeignKey(HotelCategory, on_delete=models.CASCADE, related_name='hotel_cat')
    image = models.ImageField(upload_to=path_to_hotel_image)
    rooms= models.ManyToManyField(Room)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    facilities = models.ManyToManyField(Facility)
    description = RichTextField()
    stars = models.IntegerField(null=True,blank=True,default=3)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class HotelRank(models.Model):
    user=models.ForeignKey('auth.User',null=True,on_delete=models.CASCADE)
    stars = models.IntegerField()
    hotel = models.ForeignKey(Hotel, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.hotel}->{self.stars}'
