from django.db import models

# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    place = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.IntegerField()


    def __str__(self):
        return self.name
class GALLERY(models.Model):
    name = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='profile_pics/',blank=True,null=True)
    details = models.CharField(max_length=255)
    
