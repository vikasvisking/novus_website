from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django_random_queryset import RandomManager

# Create your models here.

# catergories
class Category(models.Model):
	title = models.CharField(max_length = 30)

	def __str__(self):
		return self.title

class Blog(models.Model):
	category = models.ForeignKey(Category , on_delete = models.CASCADE)
	title = models.CharField(max_length = 100)
	author = models.CharField(max_length= 50, default = "Admin")
	content = models.TextField()
	date = models.DateField(default = datetime.now)
	image = models.ImageField(upload_to = 'blog/')
	objects = RandomManager()

	def __str__(self):
		return self.title + " | " + self.category.title 

class Contact(models.Model):
	name = models.CharField(max_length = 100)
	surname = models.CharField(max_length = 100)
	email = models.CharField(max_length = 400)
	phone = models.CharField(max_length = 100)
	message = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.name + self.surname
