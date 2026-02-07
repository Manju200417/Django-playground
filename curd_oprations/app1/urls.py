from django.urls import path
from . import views

urlpatterns = [
    path('add', views.add,name='add'),
    path('show/', views.show,name='show'),
    path('delete/', views.delete,name='delete'),
]
