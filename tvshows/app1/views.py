from django.shortcuts import render, redirect
from . models import Show
from django.contrib import messages

def index(request):
    context = {
        'shows': Show.objects.all,
    }
    return render(request, "index.html", context)


def addshow(request):
    return render(request, "addshow.html")


def submitshow(request):
    errors = Show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('shows/new')
    else:
        Show.objects.create(
            title=request.POST['title'], Network=request.POST['network'],
            release_date=request.POST['releasedate'], description=request.POST['description'])
        id = Show.objects.last().id
    return redirect('/shows/'+str(id))


def display(request, id):
    context = {
        "shows": Show.objects.get(id=id)
    }
    return render(request, "display.html", context)


def edit(request, id):
    context = {
        'shows': Show.objects.get(id=id),
    }
    return render(request, "edit.html", context)


def update(request, id):
    errors = Show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('shows/<id>/edit')
    else:
        show = Show.objects.get(id=id)
        show.title = request.POST['title']
        show.Network = request.POST['network']
        show.release_date = request.POST['releasedate']
        show.description = request.POST['description']
        show.save()
    return redirect('/shows/'+str(id))


def delete(request, id):
    Show.objects.get(id=id).delete,
    return redirect('/shows')


