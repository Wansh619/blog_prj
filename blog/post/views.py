from django.shortcuts import render
from .models import post
# Create your views here.
def home(request):
    p =post.objects.all()
    return render(request,'home.html',{'posts':p})

def read(request,pk):
    p =post.objects.get(id = pk )
    return render(request,'read.html',{'p':p})
