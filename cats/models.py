from django.db import models
from django.conf import settings


# Create your models here.
class Cats(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    name = models.CharField(max_length = 200)
    description = models.TextField()
    happiness = 10
    hunger = 0

    def pet(self):
        self.happiness = self.happiness+1
        self.save()
    
    def feed(self):
        self.hunger = self.hunger-1
        if(self.hunger<0):
            self.hunger = 0
        self.save()

    def __str__(self):
        return self.name