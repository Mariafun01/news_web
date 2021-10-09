from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'myadmin/login.html',locals())


def main(request):
    return render(request,'myadmin/main.html',locals())