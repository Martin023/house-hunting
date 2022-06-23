from django.shortcuts import redirect, render
from .forms import HouseForm
from hunter.models import House

# Create your views here.
def home(request):
    houses = House.objects.all()
    
    return render(request,'home.html',{'houses':houses})

def add_house(request):
    form = HouseForm()
    context = {'form':form}
    if request.method == 'POST':
        form=HouseForm(request.POST)
        if form.is_valid():
            house = form.save(commit=False)
            house.save()
            return redirect('homepage')

        else:
            form = HouseForm()

    return render(request,'add_house.html',context)


def get_house(request,pk):
    house = House.objects.get(id=pk)
    return render(request,'house.html',{'house':house})

def update_house(request,pk):
    house = House.objects.get(id=pk)
    form = HouseForm(request.POST,instance=house)

    if form.is_valid():
            house = form.save(commit=False)
            house.save()
            return redirect('homepage')

            
    else:
        form = HouseForm()

    context = {
        'form':form
    }

    return render(request,'update_house.html',context)

def delete_house(request,pk):
    house = House.objects.get(id=pk)
    house.delete()
    
    return redirect('homepage')