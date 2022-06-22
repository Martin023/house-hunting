from django.shortcuts import render
from .forms import HouseForm
from hunter.models import House

# Create your views here.
def home(request):
    houses = House.objects.all()
    
    return render(request,'home.html',{'houses':houses})

def add_house(request):
    form = HouseForm()
    # if request.method == 'POST':
    #     form = HouseForm(request.POST)
    #     if form.is_valid():
    #         form.save(commit=True)

    #     else me
    return render(request,'add_house.html',{'form':form})


def get_house(request,pk):
    house = House.objects.get(id=pk)
    return render(request,'house.html',{'house':house})
