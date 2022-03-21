from django.db import models
from django.contrib.auth.models import User

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
        return self.name

    @classmethod
    def search_neighbourHood(cls,searchterm):
        neighbourHood= cls.objects.filter(name__icontains=search_term)
        return neighbourHood  

class User (models.Model):
    User_name=models.CharField(max_length=255)
    neighbourHood= models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, blank=True)


    def save_User(self):
        self.save()

    def delete_User(self):
        self.delete()


class Business(models.Model):
    Business_name =models.CharField(max_length=255)
    User= models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
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
        return self.name