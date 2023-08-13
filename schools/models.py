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
        return self.middlename

    
class course(models.Model):
     img  = models.ImageField(upload_to='course', null=True)
     title = models.CharField(max_length=225)
     name = models.CharField(max_length=225, blank=False, null=True)
     details = models.CharField(max_length=255, null=True)

     class Meta:
         verbose_name_plural= 'courses'


     def __str__(self):
        return self.title




class slider(models.Model):
    image = models.ImageField( upload_to='slider')
    title = models.CharField(max_length=225, blank=True)

    class Meta:
         verbose_name_plural= 'sliders'

    def __str__(self):
        return self.title

class testmonial(models.Model):
    image = models.ImageField( upload_to='testmonial')
    name = models.CharField(max_length=225, blank=True)

    class Meta:
         verbose_name_plural= 'testmonials'

    def __str__(self):
        return self.name
