from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Customer(models.Model):
	user = models.OneToOneField(User, null=True, on_delete= models.CASCADE)
	name = models.CharField(max_length=30, blank= False, null = True)
	email = models.EmailField(max_length=30, blank=False, null = True)
	status = ( 
				("Student", "Student"),
				("Employee", "Employee"),
				("Business", "Business"),
				("Other", "Other")

				)
	category = models.CharField(choices = status, null=True, max_length= 40)

	#####################################expense = models.ForeignKey(Expense, on_delete= models.PROTECT, null = True)###################################
	date_created = models.DateTimeField(auto_now_add= True)

	def __str__(self):
		return self.name


class Expense(models.Model):
	expense_name = models.CharField(max_length=30, null = True)
	amount = models.IntegerField(blank= False)

	status_1 = (
				("important","important"),
				("normal", "normal"),
				("less important", "less important")
				)

	status_2 = (
				("Food", "Food"),
				("Social Life", "Social Life"),
				("Self-development", "Self-development"),
				("Transportation", "Transportation"),
				("Household", "Household"),
				("Apparel", "Apparel"),
				("Health","Health"),
				("Education","Education"),
				("Waste",	"Waste"),
				("Other", 	"Other")

				)

	importance = models.CharField(max_length= 30, choices = status_1)

	tags = models.CharField(max_length= 30, choices= status_2)

	description = models.CharField(max_length=30, blank = True, null = True)

	user = models.ForeignKey(Customer, null = True, on_delete= models.PROTECT)

	def __str__(self):
		return self.expense_name




