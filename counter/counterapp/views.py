from django.shortcuts import render

def index(request):
    if 'count' not in request.session:
        request.session['count']=0
    else:
        request.session['count']+=1
    return render(request , "index.html")
