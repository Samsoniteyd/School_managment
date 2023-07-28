from django.db import models

# Create your models here.


class Registration(models.Model):

    First_Name = models.CharField(max_length=225)
    Last_Name = models.CharField(max_length=225)
    middlename = models.CharField(max_length=255, null=True)
    address  = models.TextField()
    date_of_birth = models.DateField(blank=False, null=True)
    
    created = models.DateTimeField(auto_now_add=True)
   



    def __str__(self):
        pass

    
    