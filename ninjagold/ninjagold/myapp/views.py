from django.shortcuts import render, redirect
import random
from datetime import datetime


def index(request):
    if 'golden' not in request.session:
        request.session['golden'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    return render(request, "index.html")


def money(request):
    arr = ['farm', 'cave', 'house']
    location = request.POST['gold']
    color = "green"
    d = (datetime.now())
    if location in arr:
        rand = random.randint(10, 20)
        sentence = f"You entered a {location} and earned {rand} gold.{d}"
    else:
        rand = random.randint(-50, 50)
        if rand >= 0:
            sentence = f"You completed a {location} and earned {rand} gold.{d}"
        else:
            sentence = f"You failed a {location} and lost {abs(rand)} gold. Ouch {d}"
            color = "red"
    request.session['golden'] += rand
    request.session['activities'].append({'name': sentence, 'color': color})
    return redirect('/')


def clear(request):
    request.session.clear()
    return redirect('/')
