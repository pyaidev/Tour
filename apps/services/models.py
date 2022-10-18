from ckeditor.fields import RichTextField
from django.db import models


class Services(models.Model):
    title = models.CharField(max_length=211)
    avatar = models.ImageField()
    content = RichTextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Cat(models.Model):
      title = models.CharField(max_length=255)

      def __str__(self):
            return self.title


class Car(models.Model):
      name=models.CharField(max_length=255)
      cat=models.ForeignKey(Cat, null=True,on_delete=models.CASCADE)
      empty = models.BooleanField(default=False)

class Rent(models.Model):
      car=models.ForeignKey(Car, null=True, on_delete=models.CASCADE)
      where=models.CharField(max_length=255)
      start=models.DateField()
      end=models.DateField()
      price=models.IntegerField()


      def __str__(self):
            return self.car

