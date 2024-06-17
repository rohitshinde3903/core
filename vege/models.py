from django.db import models


# Create your models here.
class Receipe(models.Model):
    receipe_name = models.CharField( max_length=500)
    receipe_description = models.TextField()
    receipe_image = models.ImageField(upload_to="receipe")