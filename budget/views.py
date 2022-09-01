from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.views.decorators.http import require_http_methods

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404

# Create your views here.
#from .forms import CreateUserForm
from random import randint
#from .models import User

from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from .models import *
from .forms import CreateUserForm, ExpenseForm
from .decorators import unauthenticated_user
from django.contrib.auth.models import Group

# Create your views here.
@unauthenticated_user
def registerPage(request):

	form = CreateUserForm()
	if request.method == "POST":
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='customer')
			user.groups.add(group)

			Customer.objects.create(
					user = user,
					name = user.username,
					)
		

			messages.success(request, "Account was created for " + username)

			return redirect('login')

	context = {'form' : form}

	return render(request, 'budget/register.html', context)



@unauthenticated_user
def loginPage(request):

	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username = username, password = password)

		if user is not None:
			login(request, user)
			return redirect('home')

		else:
			messages.info(request, "username or password is incorrect")

	context = {}

	return render(request, "budget/login.html", context)

def logoutUser(request):
	logout(request)
	return redirect('login')
	
def home(request):

	quotes_list = ["                   'Money is a terrible master but an excellent servant.'~P.T. Barnum~",
					 "                 'A man who pays his bills on time is soon forgotten.'~Oscar Wilde~",
					 "                'The most difficult thing is the decision to act, the rest is merely tenacity.'~Amelia Earhart~",
					 "                'Beware of little expenses; a small leak will sink a great ship.'~Benjamin Franklin~",
					 "                'You cannot escape the responsibility of tomorrow by evading it today.'~Abraham Lincoln~",
					 "                'The desire of gold is not for gold. It is for the means of freedom and benefit.'~Ralph Waldo Emerson~",
					 "                 'To contract new debts is not the way to pay old ones.'~George Washington~",
					 "                 'Fortune befriends the bold.'~Emily Dickinson~",
					 "'                When prosperity comes, do not use all of it.'~Confucius~",
					 "                 'Do the best you can, and don’t take life too serious.'~Will Rogers"]

	num = len(quotes_list)

	quote = quotes_list[randint(0, num-1)]

	context =  { "quote":quote

					}
	return render(request, 'budget/home.html', context)
	
def index(request,pk):
	customer = Customer.objects.get(id= pk)
	expense = user.Expense.all()
		
	context = {
			"customer" : customer,
			"expense" : expense,
				}
	
	context = { "user" : user }
	return render(request, 'budget/index.html', context)

def expenseForm(request):
	form = ExpenseForm()
	if request.method == "POST":
		form = ExpenseForm(request.POST)

		if form.is_valid():
			Form = form.save()

			return redirect('home')

	context = {
				"form": form
				}

	return render(request, "budget/ExpenseForm.html", context)

###TODO###################################################################################################################################################################
# TO CREATE A DASHBOARD TO VIEW ALL THE EXPENSES ASSOCIATED WITH A CUSTOMER ie THE EXPENSE BOOK
# IN THAT DASHBOARD CRUD FUNCTIONALITIES SHOULD BE ADDED
# PROFILE PICTURE SHOULD BE ADDED TO NAVBAR 
# ON THE LEFT BLOCK OR RIGHT BLOCK PLACE A HTML CARD PROVIDING STORIES|FACTS|TIPS|RECCOMENDATIONS 