from django.db import models
from versatileimagefield.fields import VersatileImageField,PPOIField
from tinymce.models import HTMLField

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=50)
    address=models.TextField()
    message=models.TextField()

    def __str__(self):
        return self.name



class Gallery(models.Model):
    title=models.CharField(max_length=225)
    place=models.CharField(max_length=250)
    image = VersatileImageField('Image',upload_to='gallery/',ppoi_field='ppoi' )
    ppoi = PPOIField('Image PPOI')

    class Meta:
        verbose_name_plural = ("Gallery")

    def __str__(self):
        return str(self.title)



class Update(models.Model):
    title=models.CharField(max_length=225)
    summary=models.CharField(max_length=500)
    date=models.DateField()
    image=VersatileImageField('Image',upload_to='updates/',ppoi_field='ppoi' )
    ppoi = PPOIField('Image PPOI')
    content=HTMLField(blank=True, null=True)
    slug=models.SlugField(unique=True)

    def __str__(self):
        return str(self.title)



class Testimonial(models.Model):
    name=models.CharField(max_length=225)
    designation=models.CharField(max_length=225)
    decription=models.CharField(max_length=500)
    image=VersatileImageField('Image',upload_to='testimonials/',ppoi_field='ppoi' )
    ppoi = PPOIField('Image PPOI')

    def __str__(self):
        return str(self.name)