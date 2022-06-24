from django.shortcuts import redirect, render
from .forms import HouseForm
from hunter.models import House,Location
from django.contrib import messages

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

def all_houses(request):
    house = House.objects.all()
    context= {
        'house':house,
    }

    return render(request,'all_houses.html',context)

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


def get_house(request,pk):
    house = House.objects.get(id=pk)
    return render(request,'house.html',{'house':house})

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

def delete_house(request,pk):
    house = House.objects.get(id=pk)
    house.delete()

    return redirect('homepage')