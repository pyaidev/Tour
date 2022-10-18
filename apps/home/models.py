from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=211)
    avatar = models.ImageField(upload_to='person')
    location = models.CharField(max_length=211)
    content = models.TextField()

    def __str__(self):
        return self.name
