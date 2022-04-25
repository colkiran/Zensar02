from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def setsession(request):
    request.session['brndname'] = 'apple'
    request.session['product'] = 'iphone pro max'
    return render(request, 'setsession.html')

def getsession(request):
    if "brndname" in request.session:
        pname = request.session['brndname']
        prd = request.session['product']
        key = request.session.keys()
        item = request.session.items()
        prc = request.session.setdefault('price', 145000.00)
        return render(request, "getsession.html", {'brndname': pname,
                'prod': prd, 'keys': key, 'items': item, 'price': prc})
    else:
        return render(request, "getsession.html", {'brndname': "deleted",
                'prod': "deleted", 'keys': "deleted", 'items': "deleted", 'price': "deleted"})

def delsession(request):
    if "brndname" in request.session:
        request.session.clear()
    return render(request, "delsession.html")

def setssntime(request):
    request.session['brndname'] = "Samsung"
    request.session.set_expiry(0)
    return render(request, "setsessiontime.html")


def getssntime(request):
    if "brndname" in request.session:
        bname = request.session['brndname']
        return render(request, "getsessiontime.html", {'brndname': bname})
    else:
        return render(request, "getsessiontime.html", {'brndname':"Session Deleted"})


def delssntime(request):
    request.session.clear()
    return  render(request, "delsessiontime.html")
