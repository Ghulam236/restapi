from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Item
import requests

def item_list(request):
    items = Item.objects.all()
    data = [{"name": item.name, "description": item.description, "price": item.price,"discountPercentage": item.discountPercentage, "rating": item.rating, "stock": item.stock,"brand": item.brand, "category": item.category, "thumbnail": item.thumbnail,"image_urls":item.image_urls,} for item in items]
    return JsonResponse(data, safe=False)
def show_api_data_in_front(request):
    response=requests.get("http://127.0.0.1:8000/friuts").json()
    print(type(response))
    context={
        "response":response
    }
    print(response)
    return render(request,'home.html',context)


from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            # Redirect to login page or some other page upon successful registration
            return redirect('login')
    else:
        form = UserCreationForm()
        # form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


