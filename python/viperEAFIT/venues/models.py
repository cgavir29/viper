from django.db import models

# Create your models here.
class Venue(models.Model):
    name = models.CharField(max_length=25)
    address = models.CharField(max_length=120)
    email = models.EmailField()

    def __str__(self):
        return self.name