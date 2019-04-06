from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
	return render(request, 'dashboard/index.html')

def login(request):
	if request.user.is_authenticated and request.user.is_superuser:
		return HttpResponseRedirect('/dashboard')
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		userObj = auth.authenticate(username = username, password = password, request = request)
		if userObj is not None:
			auth.login(userObj)
			messages.alert-success('You are successfully logged in')
			# return HttpResponseRedirect('/dashboard')
		else:
			messages.alert-error('Invalid username or password')
			return  HttpResponseRedirect('/dashboard/login')
	return render(request, 'dashboard/login.html')
