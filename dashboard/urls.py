from django.urls import path
from dashboard import views

# app_name = 'dashboard'


urlpatterns = [
	path('', views.home , name ='home'),
	path('login/', views.login, name ='login')
]