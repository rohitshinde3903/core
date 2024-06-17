from django.db import models

# Create your models here.
class Students(models.Model):
    # id = models.AutoField()
    name = models.CharField(max_length = 150)
    age = models.IntegerField()
    Email = models.EmailField()
    adress = models.TextField(null=True)
    image = models.ImageField()
    file = models.FileField()
    
    
    
    