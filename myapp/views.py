from django.shortcuts import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1 style="text-align: center">This response is from Django application.</h1>')

