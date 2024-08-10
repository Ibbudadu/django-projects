from django.http import HttpResponse


def home(request):
    return HttpResponse(f"<h1 style='color:red'>welcome to django class</h1>")


def font_home(request):
    return HttpResponse(f'<h1>this is font page</h1>')


def vote_fun(request):
    name = 'ibbu'
    age = 15
    if age>= 18:
        return HttpResponse(f'{name} is eligible to vote')
    else:
        return HttpResponse(f'{name} is not eligible to vote')


def even_num(request):
    l1 = [1,2,3,5,9,8,14,57,46,78]
    l2 = [i for i in l1  if i%2==0 and i>0]
    return HttpResponse(f'<h1>even numbers are {l2}</h1>')