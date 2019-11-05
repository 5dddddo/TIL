from django.shortcuts import render,redirect
from .models import Student

# Create your views here.
def index(request):
    students = Student.objects.all()[::-1]
    context ={'students':students}
    return render(request, 'students/index.html',context)

def detail(request, student_pk):
    student = Student.objects.get(pk=student_pk)
    context = {'student' : student,}
    return render(request, 'students/detail.html', context)

def new(request):
    return render(request, 'students/new.html')

def create(request):
    name = request.POST.get('name')
    age = request.POST.get('age')
    major = request.POST.get('major')

    Student.objects.create(name=name, age=age, major=major)

    return redirect('/students/')

def delete(request, student_pk):
    student = Student.objects.get(pk=student_pk)
    student.delete()
    return redirect('/students/')

def edit(request, student_pk):
    student = Student.objects.get(pk=student_pk)
    context ={
        'student':student,
    }
    return render(request, 'students/edit.html', context)

def update(request, student_pk):
    student = Student.objects.get(pk=student_pk)
    name = request.POST.get('name')
    age = request.POST.get('age')
    major = request.POST.get('major')

    student.name = name
    student.age = age
    student.major = major

    student.save()

    return redirect(f'/students/{student_pk}')


