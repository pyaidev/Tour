from django.db import models
from ckeditor.fields import RichTextField
from django.utils.html import escape
# Create your models here.
class TravelTourDestinationImages(models.Model):
      image=models.ImageField()
      

      
      # def image_tag(self):
      #       return u'<img src="%s" />' % escape(self.image.url)
      # image_tag.short_description = 'TravelTourDestinationImages'
      # image_tag.allow_tags = True
      
class TravelTourDestination(models.Model):
      title = models.CharField(max_length=25)
      content=RichTextField()
      images = models.ManyToManyField(TravelTourDestinationImages)

      def __str__(self):
            return self.title

class TravelCategory(models.Model):
      title = models.CharField(max_length=25, blank=True)

      def __str__(self):
            return self.title


class Travel(models.Model):
      title = models.CharField(max_length=255 )
      location=models.CharField(max_length=255)
      image=models.ImageField(null=True)
      travel_destination=models.ManyToManyField(TravelTourDestination)
      cat=models.ManyToManyField(TravelCategory)
      stars=models.IntegerField(default=3)
      price=models.IntegerField(default=300)
      created_at=models.DateTimeField(auto_now_add=True)

      def __str__(self):
            return self.title


class TravelRank(models.Model):
    user=models.ForeignKey('auth.User',null=True,on_delete=models.CASCADE)
    stars = models.IntegerField()
    travel = models.ForeignKey(Travel, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.travel}->{self.stars}'
