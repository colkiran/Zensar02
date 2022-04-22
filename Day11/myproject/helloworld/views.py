from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("<h1> Hello World </h1>")
    return render(request, "home.html", {'gname': 'Sachin Tendulkar'})
<<<<<<< HEAD

def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])

    val3 = val1 + val2
    return render(request, 'result.html', {'res': val3})
=======
>>>>>>> origin/master
