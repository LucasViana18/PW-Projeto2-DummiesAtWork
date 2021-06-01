from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    country = models.CharField(max_length=30)
    subject = models.CharField(max_length=1000)

    def __str__(self):
        return self.first_name + " " + self.last_name
