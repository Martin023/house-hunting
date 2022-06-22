from django.shortcuts import render

from hunter.models import House

# Create your views here.
def home(request):
    houses = House.objects.all()
    context={
        'houses':houses

    }
    return render(request,'home.html',context )