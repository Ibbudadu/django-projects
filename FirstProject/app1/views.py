from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse('<h1 style= green>this is app 1</h1> ')