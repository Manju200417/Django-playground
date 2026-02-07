# from django.contrib import admin
from django.urls import path,include
from django.shortcuts import render


def dashboard(request):
    return render(request,'dashboard.html') 

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('dash/', dashboard),
    path('', include('app1.urls')),
]
