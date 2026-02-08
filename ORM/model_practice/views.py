from django.shortcuts import render
from .models import Customer

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