from django import forms
from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from chow.models import User,CustomFoods1


#reg_form
class CustomUserForm(UserCreationForm):
  first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your First Name'}))
  last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Last Name'}))
  username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your username'}))
  email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Email Address'}))
  phone_number=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Your Phone Number'}))
  password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}))
  password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Re-enter your Password'}))
  address=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your delivery Address'}))

  class Meta:
    model=User
    fields=['first_name','last_name','username','email','password1','password2','address','phone_number']

class CustomDishes(forms.ModelForm):
  class Meta:
    model=CustomFoods1
    fields=['dish_name','dish_description','dish_count','dish_picture','spice_or_sweet_level','healthier_low_kcal_version']
