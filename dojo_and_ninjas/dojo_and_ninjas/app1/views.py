from django.shortcuts import render,redirect
from .models import *
def index(request):
    context = {
        'alldojos': Dojo.objects.all()
    }
    return render(request, 'index.html',context)


def add_dojo(request):
    Dojo.objects.create(name=request.POST['name'], city=request.POST['city'], state=request.POST['state'])
    return redirect('/')

def add_ninja(request):

    Ninja.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], dojo=Dojo.objects.get(id=request.POST['dojos']))
    return redirect('/')
# Create your views here.
