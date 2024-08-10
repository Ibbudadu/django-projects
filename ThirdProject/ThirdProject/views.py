from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'index.html')

def read_fun(request):
    name = request.POST['txtname']
    age = request.POST['txtage']
    email = request.POST['txtemail']
    mobile = request.POST['txtnumber']
    place = request.POST['txtplace']
    #return HttpResponse(f'<h1>my name is {name}<br>'
    #                   f'my age is {age}<br>'
    #                   f'my email is {email}<br>'
    #                   f'my mobile number is {mobile}<br>'
    #                   f'my place is {place}</h1>')
    return render(request,'display.html', {'name': name, 'age': age, 'email': email, 'mobile': mobile, 'place': place})