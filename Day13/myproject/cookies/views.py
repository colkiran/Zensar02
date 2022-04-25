from django.shortcuts import render

# Create your views here.

def setCookie(request):
    response = render(request, "setcookie.html")
    response.set_cookie("prdname", 'Nike Shoes')
    return response

def getCookie(request):
    if 'prdname' in request.COOKIES:
        prdname = request.COOKIES['prdname']
    else:
        prdname = "Cookies deleted...."
    return render(request, "getcookie.html",  {'pname': prdname })

def delCookie(request):
    response = render(request, "deletecookie.html")
    response.delete_cookie('prdname')
    return response

