from django.urls import path
from dashboard import views

# app_name = 'dashboard'


urlpatterns = [
	path('', views.home , name ='home'),
	path('login/', views.login, name ='login'),
	path('logout/', views.logout, name ='logout'),

	# ========== categories =========== #
	path('allCategory/', views.allCategory, name = 'allCategory'),
	path('addCategory/', views.addCategory, name = 'addCategory'),
	path('editCategory/<int:pk>/', views.editCategory, name= 'editCategory'),
	path('deleteCategory/<int:pk>/', views.deleteCategory, name = 'deleteCategory'),


	# =============Blog Posts ========== #
	path('allBlogs/', views.allBlogs, name = 'allBlogs'),
	path('addBlogs/', views.addBlogs, name = 'addBlogs'),
	path('editBlogs/<int:pk>/', views.editBlogs, name = 'editBlogs'),
	path('deleteBlogs/<int:pk>/', views.deleteBlogs, name = 'deleteBlogs'),

	# ================= contacted Us =============== #
	path('allContacts/', views.allContacts, name = 'allContacts'),

]