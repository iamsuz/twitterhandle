from django.contrib import admin
from .forms import UsersForm
# Register your models here.
from .models import Users

class UsersAdmin(admin.ModelAdmin):
	list_display = ["username"]
	form = UsersForm
	
	# def __str__(self):              # __unicode__ on Python 2
 #    	return self.list_display

	# class Meta:
	# 	Model = Users
admin.site.register(Users)