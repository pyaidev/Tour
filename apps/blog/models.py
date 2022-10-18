from django.db import models


class Categories(models.Model):
    title = models.CharField(max_length=211)

    def __str__(self):
        return self.title


def path_to_blog_image(instance, filename):
    title = instance.title
    category = instance.category
    return 'blog/{0}/{1}/images/{2}'.format(category, title, filename)

class Blog(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=211)
    image = models.ImageField(upload_to='blog/')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.title