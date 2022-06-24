from django.shortcuts import redirect, render
from .forms import *
from hunter.models import House,Location
from django.contrib import messages
import datetime as dt
from django.contrib.auth import login, authenticate ,logout

from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):
    houses = House.objects.all()
    latest_item= houses.count()
    latest_house = House.objects.get(id=latest_item)
    context = {
        'houses':houses,
        'latest':latest_house
    }
    
    return render(request,'home.html',context)

@login_required(login_url='login')
def all_houses(request):
    house = House.objects.all()
    context= {
        'house':house,
    }

    return render(request,'all_houses.html',context)

@login_required(login_url='login')
def add_house(request):
    form = HouseForm()
    context = {'form':form}
    if request.method == 'POST':
        form=HouseForm(request.POST,request.FILES)
        print(request.POST.get('house_image'))
        if form.is_valid():
            house = form.save(commit=False)
            house.save()
            messages.success(request, "House saved!." )
            return redirect('homepage')

        else:
            messages.error(request, "Please check your inputs!." )
            form = HouseForm()
            

    return render(request,'add_house.html',context)

@login_required(login_url='login')
def get_house(request,pk):
    house = House.objects.get(id=pk)
    return render(request,'house.html',{'house':house})

@login_required(login_url='login')
def update_house(request,pk):
    house = House.objects.get(id=pk)
    form = HouseForm(request.POST,instance=house,files=request.FILES)

    if form.is_valid():
            house = form.save()
            # house.save()
            return redirect('homepage')

            
    else:
        form = HouseForm()

    context = {
        'form':form
    }

    return render(request,'update_house.html',context)

@login_required(login_url='login')
def delete_house(request,pk):
    house = House.objects.get(id=pk)
    house.delete()

    return redirect('homepage')


def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):

    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("login")