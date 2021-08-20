# from profile import Self
# from os import name
from django.core.checks import messages
from django.shortcuts import render, HttpResponse
from empapp.models import profile

# Create your views here.

def index(request):


    if request.method == "POST":
        name =request.POST.get('name')
        Age =request.POST.get('Age')
        height =request.POST.get('height')
        number =request.POST.get('number')
        Profile1 =profile(name=name, Age= Age, height=height, number= number)
        Profile1.save()

    return render(request, 'index.html')

