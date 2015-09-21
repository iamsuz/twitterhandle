from django.db import models

# Create your models here.
class Users(models.Model):
	username=models.CharField(max_length=50)
	first_name=models.CharField(max_length=50, default="Sujit")
	last_name=models.CharField(max_length=50, default="Mahavarkar")
	# name=models.CharField(max_length=50)