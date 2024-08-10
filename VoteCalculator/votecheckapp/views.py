from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'votevalidation.html')

def votecheck_fun(request):
    try:
        age = int(request.POST["txtage"])
        if age>0 and age<18:
            result = "not eligible to caste vote"
        elif age >= 18:
            result = "eligible to vote"

        else:
            result = 'please give proper value'
        return render(request, 'votevalidation.html',{"age":age, "res":result})
    except:
        result="please give integer value"
        return render(request, 'votevalidation.html', { "res": result})