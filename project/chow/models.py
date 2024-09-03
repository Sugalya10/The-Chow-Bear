from django.db import models
from django.contrib.auth.models import User
import os, datetime
from django.urls import reverse


#upload
def getFileName(request,filename):
  now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
  new_filename="%s%s"%(now_time,filename)
  return os.path.join('uploads/',new_filename)
 

#categories
#Sumptuous Scroll
class Menu(models.Model):
  name=models.CharField(max_length=150,null=False,blank=False)
  image=models.ImageField(upload_to=getFileName,null=True,blank=True)
  description=models.TextField(max_length=500,null=False,blank=False)
  status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
  created_at=models.DateTimeField(auto_now_add=True)
 
  def __str__(self) :
    return self.name

#Products 
class Product(models.Model):
  category=models.ForeignKey(Menu,on_delete=models.CASCADE)
  name=models.CharField(max_length=150,null=False,blank=False)
  vendor=models.CharField(max_length=150,null=False,blank=False)
  food_image=models.ImageField(upload_to=getFileName,null=False,blank=False)
  quantity=models.IntegerField(null=False,blank=False)
  price=models.FloatField(null=False,blank=False)
  is_vegetarian=models.BooleanField(default=False)
  description=models.TextField(max_length=500,null=False,blank=False)
  status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
  is_featured=models.BooleanField(default=False)
  created_at=models.DateTimeField(auto_now_add=True)
 
  def __str__(self) :
    return self.name
  

class CustomFoods1(models.Model):
  dish_name=models.CharField(max_length=150,null=False,blank=False)
  dish_description=models.CharField(max_length=1000,null=False,blank=False)
  dish_picture=models.ImageField(null=True,blank=True)
  dish_count=models.IntegerField(null=False,blank=False)
  spice_or_sweet_level=models.CharField(max_length=100,null=True,blank=True)
  healthier_low_kcal_version=models.BooleanField(max_length=20, choices=[('lowkcal', 'Low Calorie'), ('regular', 'The Usual')], default='regular')
def __str__(self) :
  return self.name
