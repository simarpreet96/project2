from django.db import models
from .validators import validate_file_extension
from django.utils import timezone
from django.conf import settings
#from django_countries.fields import CountryField
from django.utils.translation import ugettext_lazy as _ 
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

#from django.contrib.auth.models import User

class Article(models.Model):
	DRAFT='draft'
	PUBLISHED='published'
	
	STATUS_CHOICES = (
		(DRAFT,_("Draft")),
		(PUBLISHED,_("Published")),
		)

	author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	title=models.CharField(max_length=100,)
	body=models.TextField()
	status=models.CharField(choices=STATUS_CHOICES,default=DRAFT, max_length=10,)
	file = models.FileField(upload_to="documents/%Y/%m/%d", validators=[validate_file_extension])

	def __str__(self):
		return self.title

class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class City(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Details(models.Model):

    name=models.CharField(max_length=100,)
    email = models.EmailField(unique=True, null=True)
    address=models.CharField(max_length=100,)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    phone_number = models.IntegerField( blank=True ,null=True)
    zipcode = models.IntegerField( blank = True)  
    

    def __str__(self):
        return self.email


