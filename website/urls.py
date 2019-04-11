from django.urls import path
from website import views

# app_name = 'website'

urlpatterns = [	
    path('', views.home , name = 'home'),
    path('about-us/', views.aboutUs, name = 'aboutUs'),
    path('blogs/', views.blog, name = 'blog'), 
]