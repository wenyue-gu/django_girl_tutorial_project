from django.db import models
from django.conf import settings


# Create your models here.
class Cats(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    name = models.CharField(max_length = 200)
    description = models.TextField()
    happiness = 6
    hunger = 0
    hunger_status = "full"
    happiness_status = "calm"

    def pet(self):
        self.happiness = self.happiness+1
        self.save()
    
    def feed(self):
        self.hunger = self.hunger-1
        if(self.hunger<0):
            self.hunger = 0
        self.save()

    def play(self):
        self.hunger = self.hunger+1
        self.happiness = self.happiness+1
        self.save()

    def checkstatus(self):
        if(self.hunger>10):
            self.hunger_status = "very hungery"
        elif (self.hunger<5):
            self.hunger_status = "full"
        else:
            self.hunger_status = "hungry"


        if(self.happiness<3):
            self.happiness_status = "depressed"
        elif (self.happiniess<7):
            self.happiness_status = "calm"
        else:
            self.happiness_status = "estatic"

    def __str__(self):
        return self.name



    def save(self, *args, **kwargs):
        super(Cats, self).save(*args, **kwargs) # Call the "real" save() method.