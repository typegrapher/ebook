from django.db import models
from versatileimagefield.fields import VersatileImageField
from tinymce.models import HTMLField
# Create your models here.


class Product(models.Model):
    language_CHOICES = (
        ('malayalam', 'malayalam'),
        ('english', 'english'),
        ('arabic', 'arabic'),
    )
    image = VersatileImageField(upload_to = "prodect",verbose_name="upload Novel image")
    name = models.CharField(max_length=20,blank=True,null=True,verbose_name="Novel name")
    language= models.CharField(max_length=50,choices=language_CHOICES)
    author = models.CharField(max_length=20,blank=True,null=True,verbose_name="Author Name")
    price = models.IntegerField(blank=True,null=True,verbose_name="Novel price")

    class Meta:
        verbose_name = "Add Product"
        verbose_name_plural = "Add Products"

    def __str__(self):
        return str(self.name)