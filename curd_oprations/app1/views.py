from django.shortcuts import render,redirect
from .models import Student

def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')

        Student.objects.create(name = name,age = age)

    return render(request, 'app1/add_student.html')

def show(request):
    stu = Student.objects.all()
    return render(request,'app1/show_student.html',{'stu' : stu})

def delete(request):
    msg =''
    if request.method == 'GET':
        sid = request.GET.get('sid')
        
        deleted, _ = Student.objects.filter(id=sid).delete()

        if deleted:
            msg = "Student deleted successfully"
        else:
            msg = "Student not found"


    return render(request,'app1/delete_student.html',{'msg': msg})