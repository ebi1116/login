from django.db import models

# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    department = models.CharField(max_length=100)
    year = models.IntegerField()
    
    profile_image = models.ImageField(upload_to='profile_image/', blank=True, null=True)
    
    def __str__(self):
        return self.username


    
