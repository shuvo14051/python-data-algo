from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField(unique = True)
    content = models.TextField()


    def __str__(self):
        return self.title