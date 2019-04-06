from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Extending default User model   with required fields
class UserModel(models.Model):
	name = models.OneToOneField(User, on_delete = models.CASCADE)
	# image = models.ImageField(upload_to = '/profile')