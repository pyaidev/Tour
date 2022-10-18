import profile
from django.db import models

# Create your models here.


def path_to_profile_avatar(instance, filename):
    return 'profiles/{0}/{1}'.format(instance.account.username, filename)


class Profile(models.Model):
    account = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=path_to_profile_avatar)
    bio = models.TextField()

    @property
    def full_name(self):
        result = self.account.username
        if self.account.first_name and self.account.last_name:
            result = f'{self.account.first_name} {self.account.last_name}'
        return result

    def __str__(self):
        return f'{self.account.username}s profile'

class MyHotel(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    hotels = models.ForeignKey('hotels.Hotel', on_delete=models.CASCADE)
    rooms=models.ForeignKey('hotels.Room', on_delete=models.CASCADE ,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.profile.full_name

class MyTravel(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    travel = models.ForeignKey('tours.Travel', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.profile.full_name
