from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib import auth
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.

# Dashboard Homepage
@login_required
def home(request):
	return render(request, 'dashboard/index.html')


 # ================ login / logout =============== #


def login(request):
	if request.user.is_authenticated and request.user.is_superuser:
		return HttpResponseRedirect('/dashboard')
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		userObj = auth.authenticate(username = username, password = password, request = request)
		if userObj is not None:
			auth.login(request, userObj)
			messages.success(request, 'You are successfully logged in')
			return HttpResponseRedirect('/dashboard')
		else:
			messages.error(request,'Invalid username or password')
			return  HttpResponseRedirect('/dashboard/login')
	return render(request, 'dashboard/login.html')

@login_required
def logout(request):
	auth.logout(request)
	messages.success(request, 'You are successfully logged out')
	return HttpResponseRedirect('/dashboard/login')



	  # ================== Categories ===================#

# view all Category
@login_required
def allCategory(request):
	dictV = {}
	dictV['categories'] = Category.objects.all().annotate(blog_count=Count('blog'))

	return render(request, 'dashboard/allCategory.html', dictV)

# Add Category
@login_required
def addCategory(request):
	dictV = {}
	if request.method == 'POST':
		categoryForm = CategoryForm(request.POST, request.FILES)
		if categoryForm.is_valid():
			instance = categoryForm.save()
			messages.success(request, '{} has been successfully added'.format(instance.title))
			return HttpResponseRedirect('/dashboard/allCategory')
		else:
			if categoryForm.errors:
				for field in categoryForm:
					for error in field.errors:
						messages.error(request, '{} : {}'.format(field.name, error))
	dictV['categoryForm'] = CategoryForm()
	return render(request, 'dashboard/addCategory.html', dictV)

# edit category
@login_required
def editCategory(request, pk):
	if request.method == "POST":
		instance = Category.objects.get(pk = pk)
		instance.title = request.POST.get('title')
		instance.save()
		return HttpResponseRedirect("/dashboard/allCategory")


# delete category
@csrf_exempt
@login_required
def deleteCategory(request, pk):
	if request.method == 'POST':
		category = Category.objects.get(pk = pk)
		category.delete()
		return HttpResponseRedirect('/dashboard/allCategory')


	# ================== Blogs =================== #

# view all blogs
@login_required
def allBlogs(request):
	dictV = {}
	dictV['blogs'] = Blog.objects.all()
	return render(request, 'dashboard/allblogs.html', dictV)

# add blogs
@login_required
def addBlogs(request):
	dictV = {}
	if request.method == 'POST':
		form = BlogForm(request.POST, request.FILES)
		print(request.POST)
		if form.is_valid():
			instance = form.save()
			messages.success(request, '{} has been successfull published'.format(instance.title))
			return HttpResponseRedirect('/dashboard/allBlogs')
		else:
			if form.errors:
				for field in form:
					for error in field.errors:
						messages.error(request, '{} {}'.format(field.name, error))
						data = '{} {}'.format(field.name, error)
						return JsonResponse(data, safe= False)
	dictV['form'] = BlogForm()
	dictV['categories'] = Category.objects.all()
	return render(request, 'dashboard/addBlogs.html', dictV)

# edit blogs
@login_required
def editBlogs(request, pk):
	dictV = {}
	instance = Blog.objects.get(pk = pk)
	if request.method == 'POST':
		form = BlogForm(request.POST, request.FILES, instance = instance)
		if form.is_valid():
			instance = form.save()
			messages.success(request, '{} has been successfull Edited'.format(instance.title))
			return HttpResponseRedirect('/dashboard/allBlogs')
		else:
			if form.errors:
				for field in form:
					for error in field.errors:
						messages.error(request, '{}: {}'.format(field.name, error))
	dictV['form'] = BlogForm(instance = instance)
	dictV['pk'] = pk
	dictV['categories'] = Category.objects.all()
	return render(request, 'dashboard/editBlog.html', dictV)

# delete blog post
@login_required
def deleteBlogs(request, pk):
	if request.method == 'POST':
		post = Blog.objects.get(pk = pk)
		post.delete()
		return HttpResponseRedirect('/dashboard/allBlogs')

# ================= Contacts =================== #

# contact
@login_required
def allContacts(request):
	dictV = {}
	dictV['contacts'] = Contact.objects.all()
	return render(request, 'dashboard/allContact.html', dictV)

	


