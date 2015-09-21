# from django.shortcuts import render

# # Create your views here.
# def home(request):
# 	return render(request, "home.html",{})
from .forms import UsersForm
from django.shortcuts import render
def home(request):
	title= 'Welcome'
	# if request.user.is_authenticated():
	# 	title = "My title %s" %(request.user)
	form = UsersForm(request.POST or None)
	context = {
		"title": title,
		"form":form
	}
	if form.is_valid():
		instance = form.save(commit=False)
		username = form.cleaned_data.get("username")
		first_name = form.cleaned_data.get("first_name")
		print username
		instance.save()
		context = {
			"title": "Thank you "+str(first_name),
			"twitter": "https://twitter.com/"+str(username)
		# "url":"https://twitter.com/%s",username
		# "form":form
		}
	return render(request, "form.html", context)