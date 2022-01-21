from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)
    date = models.DateTimeField()
    image = models.ImageField(blank=True,upload_to='blog/images')
    def __str__(self):
        return self.title
# Create your models here.
