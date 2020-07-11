from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.


#this is for one to one relationship of models

class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)# it will set the one-to-one field for user
    #on_delete is used for deleting the  profile if user is deleted..but if profile is deleted then it didnt delete user.
    image=models.ImageField(default='default.jpg',upload_to='profile.pics')#upload_to is create an directory which stores the imges..



    def __str__(self):
        return f'{self.user.username} profile'


    #want to svae the images and resize it..
    def save(self):
        super().save()# it will save that images

        img=Image.open(self.image.path)#it will open current image ians save it into img


        if img.height>300 or img.width>300:
            output_size=(300,300)#maximum size
            img.thumbnail(output_size)#resized image
            img.save(self.image.path)#it will store an images....override that images
