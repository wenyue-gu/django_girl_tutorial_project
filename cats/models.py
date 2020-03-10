from django.db import models
from django.conf import settings


# Create your models here.
class Cats(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    name = models.CharField(max_length = 200)
    description = models.TextField()
    happiness = models.DecimalField(default =6, max_digits=2, decimal_places=0)
    hunger = models.DecimalField(default =3, max_digits=2, decimal_places=0)
    count = models.DecimalField(default =0, max_digits=2, decimal_places=0)
    hunger_status = "full"
    happiness_status = "calm"

    def pet(self):
        self.happiness = self.happiness+1
        self.hunger = self.hunger+1
        self.checkstatus()
        self.save()
    
    def feed(self):
        self.hunger = self.hunger-1
        if(self.hunger<0):
            self.hunger = 0
        self.checkstatus()
        self.save()

    def play(self):
        self.hunger = self.hunger+2
        self.happiness = self.happiness+2
        self.checkstatus()
        self.save()

    def time(self):
        self.count = self.count+1
        if(self.count>5):
            self.hunger = self.hunger+1
            self.happiness = self.happiness-1
            if(self.happiness<0):
                self.happiness = 0
            self.count = 0
        self.checkstatus()
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
        elif (self.happiness<7):
            self.happiness_status = "calm"
        else:
            self.happiness_status = "estatic"

    def __str__(self):
        return self.name


