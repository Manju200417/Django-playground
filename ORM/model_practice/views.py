from django.shortcuts import render,redirect
from .models import Customer,Item

# Create your views here.

def add_cust(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        customer = Customer.objects.create(
            name = name,
            email = email,
            password = password
        )
    return render(request,'add_cust.html') 


def items(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        Item.objects.create(name = name,price = price) 
        return redirect('/items')
    
    items = Item.objects.all()

    return render(request,'item.html',{'items' : items})
