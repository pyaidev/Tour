from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=211)
    phone = models.CharField(max_length=211)
    email = models.EmailField()
    subject = models.CharField(max_length=211)
    message = models.TextField()

    def __str__(self):
        return self.name
