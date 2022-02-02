from urllib import request
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request,'templates\frontend\index.html')