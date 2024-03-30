from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)




class Image(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
from django.db import models

class UploadedImage(models.Model):
    name = models.CharField(max_length=100)
    caption = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
class UploadedImage(models.Model):
    name = models.CharField(max_length=100)
    caption = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
