from django.urls import include,path
from django.shortcuts import render

def home(request):
    if request.method == 'POST' or 'GET':
        name = request.POST.get('name')
        email = request.POST.get('email')
        data = {
            'name':name,
            'email':email
        }
    return render(request,'home.html',data)


def about(request,age):
    name = request.GET.get('name')
    email = request.GET.get('email')

    userdata = {
        'age':age,
        "Name":name,
        "Email":email
    }
    return render(request,'about.html',userdata)

urlpatterns = [
    path('about/<int:age>/',about),
    path('',include('core.urls')),
]
