from django.shortcuts import render
from django.http import HttpResponse
from Select import *

def index(request):
    return HttpResponse("Hello, world.")


# def getname(request):
# 	return 
