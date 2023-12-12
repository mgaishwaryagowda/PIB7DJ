from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .forms import studentform
from .models import students

# Create your views here.
form=studentform()
my_dict={"insert_me":"Its lowest...","sr":"Star dust",'n':300,'form':form}

def index(request):
    return HttpResponse("<h1>I started learning Django and its fun </h1>")

def Hello(request):
    #return HttpResponse("<h2>I am coming from the application urls.py file </h2>")
    if request.method=="POST":
        form=studentform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=studentform()
    #return render(request,'update.html',{'form':form})
    return render(request,'Hello/Home.html',context=my_dict)

def list_view(request):
    context={}
    context["dataset"]=students.objects.all() #students class it took all objects from students and it is in form of list

    return render(request,'Hello/list_view.html',context)