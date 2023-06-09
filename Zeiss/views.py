from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
import json
from django.shortcuts import get_object_or_404
import pandas as pd
import datetime

def hello(request):
    return HttpResponse("Hello world ! ")

def input(request):
    return render(request, 'input.html')
    # return render(request, './input1.html', locals())

def comment(request):
    context = request.POST['context']
    # 写入数据库
    print(context)
    return render(request, 'comment.html')

def result(request):
    # Get latest result
    return render(request, 'result.html')

