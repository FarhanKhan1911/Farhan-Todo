from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


# Now to create users profile first we need to create the model for it as below
# In model we will have to data 1. user 2. image
# we have onetoonefield with user means that this table is linked to the User that is created on that instance (User id django default table) 
# and image will have imagefield with the default image  as default.img that you have to define in media folder. Note: don't put the img in profile_pic folder
# now whenever user is created from apps.py file the signal will be generated that is define in signals.py
# the models.py will store the information but will not generate it automatically
# to generate it will be define the commands in signals.py file 

# Path that will be followed

# User created from register page                     then it will goto                            in signals.py we have commands to        the data will be store 
# using UserRegisterForm                        --->  apps.py where we have ready function     --> create the user profile and then   -->   in models.py
# (edit of default UserCreationForm in forms.py)       that will generate command for signals.py    save the user profile


'''
onetoone one to one
foreignkey one to many
manytomany 
'''

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return self.user.username   # this is to give the data in profile.html file


   