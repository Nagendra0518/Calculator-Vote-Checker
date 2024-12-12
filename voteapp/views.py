from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'votevalidation.html')


def votecheck_home(request):
    try:
        age = int(request.POST["txtage"])
        if age > 0 and age < 18:
            result = "not eligible to cast vote"
        elif age >= 18:
            result = "eligible for vote casting"
        else:
            result = "give proper value"
        return render(request,'votevalidation.html',{"age":age,"res":result})
    except:
        result = "please give integer value"
        return render(request,'votevalidation.html',{"res":result})