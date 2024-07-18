from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model

User = get_user_model() # because we make custom user model by Abstractuser class

@login_required(login_url="/login/")
def receipes(request):

    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_image=receipe_image,
        )
        return redirect('/receipes/')


    queryset = Receipe.objects.all()

    # for searching food & without POSTmethod
    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))


    context = {'receipes' : queryset}
    return render(request , "receipes.html" , context)

def update_receipe(request , slug):
    queryset = Receipe.objects.get(slug=slug)

    if request.method == "POST":
        data=request.POST

        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        queryset.receipe_name=receipe_name
        queryset.receipe_description=receipe_description
        if receipe_image:
            queryset.receipe_image = receipe_image
        queryset.save()
        return redirect('/receipes/')
    context = {'receipes' : queryset}
    return render(request , "update_receipe.html" , context)



def delete_receipe(request , slug):
    queryset = Receipe.objects.get(slug=slug)
    queryset.delete()
    return redirect('/receipes/')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.info(request , 'invalid username')
            return redirect('/login/')

        user = authenticate(username = username , password = password)
        if user is None:
            messages.info(request , 'invalid password')
            return redirect('/login/')
        else:
            login(request , user)
            return redirect('/receipes/')

    return render(request , "login.html")


def logout_page(request):
    logout(request)
    return redirect('/login/')


def register(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request , 'username already taken')
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )
        password=user.set_password(password)
        user.save()
        messages.info(request , 'account created successfully')

        return redirect('/register/')

    return render(request , "register.html")

from django.db.models import Q , Sum  #for searching a perticular word in two or more columns

def get_student(request):

    queryset = Student.objects.all()
    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = queryset.filter(
            Q(student_name__icontains = search) |
            Q(department__department__icontains = search) |
            Q(student_id__student_id__icontains = search) |
            Q(student_age__contains = search) |
            Q(student_email__icontains = search)
        )

    paginator = Paginator(queryset , 10)
    page_number = request.GET.get("page" , 1)
    page_obj = paginator.get_page(page_number)

    context = {"queryset" : page_obj}
    return render(request , 'report/student.html' , context=context)


def see_marks(request , student_id):
    queryset = SubjectMarks.objects.filter(student__student_id__student_id = student_id)
    total_marks = queryset.aggregate(total_marks = Sum('marks'))

    current_rank = -1
    ranks = Student.objects.annotate(marks = Sum('studentmarks__marks')).order_by('-marks' , '-student_age')

    i = 1
    for rank in ranks:
        if student_id == rank.student_id.student_id:
            current_rank = i
            break
        i = i + 1

    return render(request , "report/see_marks.html" , {'queryset' : queryset , 'total_marks' : total_marks , 'current_rank' : current_rank})