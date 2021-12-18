from django.db import models

# Create your models here.
class Shoe(models.Model):
    shoe_name = models.CharField(max_length=55)
    price = models.IntegerField()
    shoe_colour = models.CharField(max_length=100)
    shoe_description = models.TextField()
    available_now = models.BooleanField()

    def __str__(self):
        return self.shoe_name+" - "+self.shoe_colour+" - "+str(self.available_now)