from django.db import models
from django.contrib.auth.models import User
# from cloudinary.models import CloudinaryField


# # Create your models here.

class NeighbourHood(models.Model):
    Name=models.CharField(max_length=255)
    Location = models.CharField(max_length=255)
    Occupants=models.Integer()
    Admin = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def save_neighbourHood(self):
        self.save()

    def delete_neighbourHood(self):
        self.delete()

    @classmethod
    def find_neighbourHood(request,NeighbourHood):
        try:
            project = NeighbourHood.objects.get(pk=id)

        except ObjectDoesNotExist:
            raise Http404()
    def __str__(self):
        return self.name

    @classmethod
    def search_neighbourHood(cls,searchterm):
        projects = cls.objects.filter(name__icontains=search_term)
        return projects   
        