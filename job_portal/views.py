# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import FAQ

# Create your views here.

def faq(request):
    all = FAQ.objects.all()
    return render(request, 'faq.html',{'faq':all})
def about(request):
    return render(request,'about.html')