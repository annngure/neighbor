from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
import datetime as dt
# Create your models here.

class NeighbourHood(models.Model):
    Name=models.CharField(max_length=255)
    Location = models.CharField(max_length=255)
    Occupants=models.IntegerField()
    Admin= models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
   

    def save_neighbourHood(self):
        self.save()

    def delete_neighbourHood(self):
        self.delete()

    @classmethod
    def find_neighbourHood(request,NeighbourHood):
        try:
            neighbourHood = NeighbourHood.objects.get(pk=id)

        except ObjectDoesNotExist:
            raise Http404()

    def __str__(self):
        return self.Name

    @classmethod
    def search_neighbourHood(cls,searchterm):
        neighbourHood= cls.objects.filter(name__icontains=search_term)
        return neighbourHood  

class Business(models.Model):
    Business_name =models.CharField(max_length=100)
    Owner_name = models.CharField(max_length=100, default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=True)
    Business_email = models.EmailField()
    

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def find_business(request,Business):
        try:
            business= Business.objects.get(pk=id)

        except ObjectDoesNotExist:
            raise Http404()

    def __str__(self):
        return self.Business_name

class Profile(models.Model):
    name= models.CharField(max_length=100,null=True)
    occupation= models.CharField(max_length=100,null=True)
    profile_image = models.ImageField(upload_to = 'image/', blank=True)
    Location = models.CharField(max_length=255, null=True)
    email=models.EmailField()
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
    
    def __str__(self):
        return self.bio
    

class Posts(models.Model):
    post = HTMLField(null=True)
    pub_date = models.DateTimeField(auto_now_add=True)    
    Location = models.CharField(max_length=255, null = True)
    business = models.ForeignKey(Business,on_delete=models.CASCADE, null=True)
    Owner_name = models.CharField(max_length=100, null=True)


    def save_post(self):
        self.save()
    
    def delete_post(self):
        self.delete()
    
    def __str__(self):
        return self.post