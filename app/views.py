from django.shortcuts import render

# Create your views here.

def specific(request):
    return render(request,'specific.html')