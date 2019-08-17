from django.shortcuts import render

def index(request):
    return render(request,'personal/home.html')

def contact(request):
    return render(request,'personal/basic.html',{'content':['Please contact me at hardikthakur30@gmail.com']})
