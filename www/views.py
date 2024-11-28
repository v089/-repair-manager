from django.shortcuts import render
from django.conf import settings
from .models import *
def index(request):
    context={

    }
    return render(request, 'index.html', context=context)
# Create your views here.
