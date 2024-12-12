from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'calculator.html')


def read_home(request):
    n1 = int(request.POST["textnum1"])
    n2 = int(request.POST["textnum2"])
    operation = request.POST["operation"]
    if operation == "Add":
        result = n1 + n2
    elif operation == "Sub":
        result = n1 - n2
    elif operation == "Mul":
        result = n1 * n2
    else:
        try:
            result = n1 / n2
        except:
            result = "n2 is 0 please change"
    return render(request,'calculator.html',{"n1":n1,"n2":n2,"res":result})