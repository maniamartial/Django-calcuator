from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "calculate/home.html")


def add(request):
    num1 = int(request.GET['num1'])
    num2 = int(request.GET['num2'])
    result = num1 + num2
    context = {'result': result}
    return render(request, "calculate/result.html", context)
