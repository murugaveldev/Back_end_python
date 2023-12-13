from django.shortcuts import render
from django.http import HttpResponse
from .models import datas

# Create your views here.

def index(request):
    if request.method== 'POST':
        Name=request.POST['name']
        Age=request.POST['age']
        Address=request.POST['address']
        Contact=request.POST['contact']
        Mail=request.POST['email']
        

        obj=datas()
        obj.Name=Name
        obj.Age=Age
        obj.Address=Address
        obj.Contact=Contact
        obj.Mail=Mail
        
        obj.save()

    return render(request , "index.html")






# def home(request):
#     return HttpResponse("hello world!")
