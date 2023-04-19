from django.shortcuts import render, HttpResponse , redirect

def index(request):
    return render(request, "index.html")

def save(request):
    request.session['fname'] = request.POST['fname']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect ("/result")

def show(request):
    return render(request, "result.html")