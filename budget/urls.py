from django.urls import path

from . import views

urlpatterns = [
				path('', views.home, name="home"),
				path('index/<int:pk>', views.index, name = "index"),
				path('login/', views.loginPage, name = "login"),
				path('register/', views.registerPage, name = "register"),
				path('logout/', views.logoutUser, name= "logout"),
				path('expense_form/', views.expenseForm, name= "expenseForm")










]