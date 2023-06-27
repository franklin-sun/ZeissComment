from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
import json
from django.shortcuts import get_object_or_404
import pandas as pd
import datetime
from Zeiss import functions, nlptest

def hello(request):
    return HttpResponse("Hello world ! ")

def input(request):
    return render(request, 'input.html')
    # return render(request, './input1.html', locals())

def comment(request):
    context = request.POST['context']
    name = request.POST['name']
    if name == '':
        name = '匿名用户'
    date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # 写入数据库
    print(name, context, date_time)
    functions.write_db(name, context, date_time)
    return render(request, 'comment.html')

def result(request):
    # Get latest result
    fc = functions.read_db()
    comment1,comment2,comment3 = fc.get_comments()
    nlptest
    return render(request, 'result.html', {"comment1": comment1, "comment2": comment2, "comment3": comment3})

