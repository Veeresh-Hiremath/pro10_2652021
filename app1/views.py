from django.shortcuts import render

def index(request):
    return render(request, "samp1.html")

def index2(request):
    return render(request,"samp2.html")

# Create your views here.
