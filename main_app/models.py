from django.db import models

# Create your models here.

class Property(models.Model):
    name = models.CharField(max_length = 100)
    address = models.CharField(max_length = 200)
    description = models.CharField(max_length = 500)
    value = models.IntegerField()

    def __str__(self):
        return self.name