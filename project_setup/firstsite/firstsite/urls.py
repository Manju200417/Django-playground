from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    print(request.method)
    return HttpResponse("Hello World from First Site!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mm/', home),
]




